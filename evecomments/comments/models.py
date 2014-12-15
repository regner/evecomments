

from evecomments.extensions import db

# Need to import for the foreign key to be detected properly by migration scripts
from evecomments.user.models  import UserModel
from evecomments.sites.models import SiteModel


class CommentModel(db.Model):
    """ Model for individual comments to be placed in the comments table. """

    __tablename__ = 'comments'

    id                = db.Column(db.Integer, primary_key=True)
    site_id           = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
    site              = db.relationship('SiteModel', backref=db.backref('comments', lazy='dynamic'))
    author_id         = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author            = db.relationship('UserModel', backref=db.backref('comments', lazy='dynamic'))
    message           = db.Column(db.Text, nullable=False)
    deleted           = db.Column(db.Boolean, default=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    parent            = db.relationship('CommentModel', backref=db.backref('children', lazy='dynamic'), remote_side='CommentModel.id')
    created_on        = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, site, message, author):
        self.site    = site
        self.message = message
        self.author  = author

    def __repr__(self):
        return '<CommentModel %s>' % self.id