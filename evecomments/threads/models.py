

from evecomments.extensions import db

# Need to import for the foreign key to be detected properly by migration scripts
from evecomments.sites.models   import SiteModel


class ThreadModel(db.Model):
    """ Model for individual threads to be placed in the threads table. """

    __tablename__ = 'threads'

    id      = db.Column(db.String(50), primary_key=True)
    title   = db.Column(db.String(50))
    url     = db.Column(db.Integer)

    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
    site    = db.relationship('SiteModel', backref=db.backref('threads', lazy='dynamic'))

    def __init__(self, thread_id, thread_title, thread_url, site):
        self.id    = thread_id
        self.title = thread_title
        self.url   = thread_url
        self.site  = site

    def __repr__(self):
        return '<ThreadModel %s>' % self.id