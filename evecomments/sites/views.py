

from flask           import Blueprint, render_template, abort
from flask.ext.login import login_required, current_user

from evecomments.extensions   import db
from evecomments.sites.forms  import AddSiteForm
from evecomments.sites.models import SiteModel

blueprint = Blueprint('sites', __name__, static_folder='../static')


@blueprint.route('/sites/', methods=('GET', 'POST'))
@login_required
def all_sites():
    add_site_form = AddSiteForm()

    if add_site_form.validate_on_submit():
        new_site = SiteModel(add_site_form.name.data, current_user.get_id())
        db.session.add(new_site)
        db.session.commit()

    sites = SiteModel.query.filter_by(owner=current_user.get_id()).all()

    template_values = {
        'sites'         : sites,
        'add_site_form' : add_site_form,
    }

    return render_template('sites/all_sites.html', template_values=template_values)


@blueprint.route('/sites/<int:site_id>/', methods=('GET', ))
@login_required
def site_details(site_id):
    site = SiteModel.query.filter_by(id=site_id, owner=current_user.get_id()).first()

    if site is None:
        abort(404)

    template_values = {
        'site' : site,
    }

    return render_template('sites/site_details.html', template_values=template_values)