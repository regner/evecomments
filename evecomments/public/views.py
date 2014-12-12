

from flask import Blueprint, request, session, redirect, render_template, url_for

from evecomments.extensions import oauth

blueprint = Blueprint('public', __name__, static_folder='../static')

evesso = oauth.remote_app('evesso', app_key='EVESSO')


@blueprint.route('/')
def home():
    return render_template('public/home.html')


@blueprint.route("/login")
def login():
    return evesso.authorize(callback=url_for('public.authorized', _external=True))


@blueprint.route('/callback')
def authorized():
    resp = evesso.authorized_response()

    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )

    if isinstance(resp, Exception):
        return 'Access denied: error=%s' % str(resp)

    session['evesso_token'] = (resp['access_token'], '')
    verify                  = evesso.get("verify")
    session['character']    = verify.data

    return redirect(url_for("public.home"))


@evesso.tokengetter
def get_evesso_oauth_token():
    return session.get('evesso_token')