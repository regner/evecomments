

from evecomments.extensions import db

# Need to import for the foreign key to be detected properly by migration scripts
from evecomments.sites.models import SiteModel


class CommentModel(db.Model):
    """ Model for individual comments to be placed in the comments table. """

    __tablename__ = 'comments'

    id                = db.Column(db.Integer, primary_key=True)
    site_id           = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
    site              = db.relationship('SiteModel', backref=db.backref('comments', lazy='dynamic'))
    message           = db.Column(db.Text, nullable=False)
    deleted           = db.Column(db.Boolean, default=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    parent            = db.relationship('CommentModel', backref=db.backref('children', lazy='dynamic'), remote_side='CommentModel.id')

    def __init__(self, site, message):
        self.site    = site
        self.message = message

    def __repr__(self):
        return '<CommentModel %s>' % self.id