

from flask           import Blueprint, render_template, abort, request
from flask.ext.login import current_user

from evecomments.comments.forms   import AddCommentForm
from evecomments.comments.models  import CommentModel
from evecomments.sites.models     import SiteModel
from evecomments.threads.models   import ThreadModel
from evecomments.decorators.login import login_required_for_post
from evecomments.extensions       import db

blueprint = Blueprint('comments', __name__, static_folder='../static')


@blueprint.route('/comments/embed', methods=('GET', 'POST', ))
@login_required_for_post
def embed():
    try:
        config = {
            'site_id'      : request.args['ec_site_id'],
            'thread_id'    : request.args['ec_thread_id'],
            'thread_title' : request.args['ec_thread_title'],
            'thread_url'   : request.args['ec_thread_url'],
        }

    except KeyError:
        abort(400, 'Please ensure all request parameters have been specified.')

    site = SiteModel.query.filter_by(id=config['site_id']).first()

    if site is None:
        abort(404, 'The specified site was not found.')

    add_comment_form = AddCommentForm()

    if add_comment_form.validate_on_submit():
        thread = ThreadModel.query.filter_by(id=config['thread_id']).first()

        if thread is None:
            thread = ThreadModel(config['thread_id'], config['thread_title'], config['thread_url'], site)

            db.session.add(thread)
            db.session.commit()

        new_comment = CommentModel(site, add_comment_form.message.data, current_user, thread)

        db.session.add(new_comment)
        db.session.commit()

    comments = CommentModel.query.filter_by(site_id=config['site_id']).all()

    template_values = {
        'comments'         : comments,
        'add_comment_form' : add_comment_form,
    }

    return render_template('comments/embed.html', template_values=template_values)

