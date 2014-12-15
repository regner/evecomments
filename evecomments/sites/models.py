

from evecomments.extensions import db


class SiteModel(db.Model):
    """ Model for individual sites to be placed in the sites table. """

    __tablename__ = 'sites'

    id    = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(50))
    owner = db.Column(db.Integer)

    def __init__(self, name, owner):
        self.name  = name
        self.owner = owner

    def __repr__(self):
        return '<SiteModel %s>' % self.id