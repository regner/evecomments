

from flask           import Blueprint, render_template, abort
from flask.ext.login import login_required, current_user

from evecomments.extensions    import db
from evecomments.sites.forms   import AddSiteForm, EditSiteForm
from evecomments.sites.models  import SiteModel
from evecomments.threads.forms import EditThreadForm

blueprint = Blueprint('sites', __name__, static_folder='../static')


@blueprint.route('/sites/', methods=('GET', 'POST'))
@login_required
def all_sites():
    add_site_form = AddSiteForm()

    if add_site_form.validate_on_submit():

        new_site = SiteModel(add_site_form.id.data, add_site_form.name.data, current_user)

        db.session.add(new_site)
        db.session.commit()

    sites = SiteModel.query.filter_by(owner=current_user).all()

    template_values = {
        'sites'         : sites,
        'add_site_form' : add_site_form,
    }

    return render_template('sites/all_sites.html', template_values=template_values)


@blueprint.route('/sites/<string:site_id>/details/', methods=('GET', 'POST'))
@login_required
def site_details(site_id):
    site = SiteModel.query.filter_by(id=site_id, owner=current_user).first()

    if site is None:
        abort(404)

    edit_site_form = EditSiteForm()

    if edit_site_form.validate_on_submit():
        site.name = edit_site_form.name.data

        db.session.commit()

    template_values = {
        'site'           : site,
        'edit_site_form' : edit_site_form,
    }

    return render_template('sites/site_details.html', template_values=template_values)


@blueprint.route('/sites/<string:site_id>/comments/', methods=('GET', ))
@login_required
def site_comments(site_id):
    site = SiteModel.query.filter_by(id=site_id, owner=current_user).first()

    if site is None:
        abort(404)

    template_values = {
        'site' : site,
    }

    return render_template('sites/site_comments.html', template_values=template_values)


@blueprint.route('/sites/<string:site_id>/threads/', methods=('GET', ))
@login_required
def site_threads(site_id):
    site = SiteModel.query.filter_by(id=site_id, owner=current_user).first()

    if site is None:
        abort(404)

    edit_thread_form = EditThreadForm()

    template_values = {
        'site'              : site,
        'edit_thread_form' : edit_thread_form,
    }

    return render_template('sites/site_threads.html', template_values=template_values)