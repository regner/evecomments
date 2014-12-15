

from datetime import datetime

from flask           import Blueprint, request, session, redirect, url_for, render_template
from flask.ext.login import login_user, logout_user

from evecomments.user.models import UserModel
from evecomments.extensions  import oauth, db, login_manager

blueprint = Blueprint('user', __name__, static_folder='../static')
evesso    = oauth.remote_app('evesso', app_key='EVESSO')


@blueprint.route("/login")
def login():
    return evesso.authorize(callback=url_for('user.authorized', _external=True))


@blueprint.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('public.home'))


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
    verify                  = evesso.get('verify')

    user = UserModel.query.filter_by(id=verify.data['CharacterID']).first()

    if user is None:
        user = UserModel(verify.data['CharacterID'], verify.data['CharacterName'], verify.data['CharacterOwnerHash'])
        user.login_count = 0
        user.join_date   = datetime.now()

    user.login_count += 1

    db.session.add(user)
    db.session.commit()

    login_user(user)

    return render_template('user/callback.html')


@evesso.tokengetter
def get_evesso_oauth_token():
    return session.get('evesso_token')


@login_manager.user_loader
def load_user(character_id):
    """ Required callback for Flask-Login. Returns the user DB object or None. """

    user = UserModel.query.filter_by(id=character_id).first()

    return user