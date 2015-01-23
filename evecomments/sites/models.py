

from evecomments.extensions import db

# Need to import for the foreign key to be detected properly by migration scripts
from evecomments.user.models import UserModel


class SiteModel(db.Model):
    """ Model for individual sites to be placed in the sites table. """

    __tablename__ = 'sites'

    id       = db.Column(db.String(50), primary_key=True)
    name     = db.Column(db.String(50))

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner    = db.relationship('UserModel', backref=db.backref('sites', lazy='dynamic'))

    def __init__(self, site_id, name, owner):
        self.id    = site_id
        self.name  = name
        self.owner = owner

    def __repr__(self):
        return '<SiteModel %s>' % self.id