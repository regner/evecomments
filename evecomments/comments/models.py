

from evecomments.extensions import db

# Need to import for the foreign key to be detected properly by migration scripts
from evecomments.sites.models import SiteModel


class CommentModel(db.Model):
    """ Model for individual comments to be placed in the comments table. """

    __tablename__ = 'comments'

    id      = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'))
    site    = db.relationship('SiteModel', backref=db.backref('comments', lazy='dynamic'))

    def __init__(self, site):
        self.site = site

    def __repr__(self):
        return '<CommentModel %s>' % self.id