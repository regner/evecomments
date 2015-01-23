

from evecomments.extensions import db

# Need to import for the foreign key to be detected properly by migration scripts
from evecomments.user.models    import UserModel
from evecomments.sites.models   import SiteModel
from evecomments.threads.models import ThreadModel


class CommentModel(db.Model):
    """ Model for individual comments to be placed in the comments table. """

    __tablename__ = 'comments'

    id                = db.Column(db.Integer,  primary_key=True)
    message           = db.Column(db.Text,     nullable=False)
    deleted           = db.Column(db.Boolean,  default=False)
    created_on        = db.Column(db.DateTime, default=db.func.now())

    site_id           = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
    site              = db.relationship('SiteModel', backref=db.backref('comments', lazy='dynamic'))

    author_id         = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author            = db.relationship('UserModel', backref=db.backref('comments', lazy='dynamic'))

    thread_id         = db.Column(db.String, db.ForeignKey('threads.id'), nullable=False)
    thread            = db.relationship('ThreadModel', backref=db.backref('comments', lazy='dynamic'))

    parent_comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    parent            = db.relationship('CommentModel', backref=db.backref('children', lazy='dynamic'), remote_side='CommentModel.id')

    def __init__(self, site, message, author, thread):
        self.site    = site
        self.message = message
        self.author  = author
        self.thread  = thread

    def __repr__(self):
        return '<CommentModel %s>' % self.id