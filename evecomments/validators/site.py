

from wtforms import ValidationError

from evecomments.sites.models import SiteModel


def unique_site_id(form, field):
    """ Validates that a site ID string does not already exist in the DB. """

    site = SiteModel.query.filter_by(id=field.data).all()

    if site is not None and len(site) > 0:
        raise ValidationError('Site ID is already in use.')