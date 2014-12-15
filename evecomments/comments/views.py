

from flask           import Blueprint, render_template, abort
from flask.ext.login import current_user

from evecomments.comments.forms   import AddCommentForm
from evecomments.comments.models  import CommentModel
from evecomments.sites.models     import SiteModel
from evecomments.decorators.login import login_required_for_post
from evecomments.extensions       import db

blueprint = Blueprint('comments', __name__, static_folder='../static')


@blueprint.route('/comments/<int:site_id>/embed', methods=('GET', 'POST', ))
@login_required_for_post
def embed(site_id):
    site = SiteModel.query.filter_by(id=site_id).first()

    if site is None:
        abort(404)

    add_comment_form = AddCommentForm()

    if add_comment_form.validate_on_submit():
        new_comment = CommentModel(site, add_comment_form.message.data, current_user)

        db.session.add(new_comment)
        db.session.commit()

    comments = CommentModel.query.filter_by(site_id=site_id).all()

    print comments[-1].message

    template_values = {
        'site_id'          : site_id,
        'comments'         : comments,
        'add_comment_form' : add_comment_form,
    }

    return render_template('comments/embed.html', template_values=template_values)

