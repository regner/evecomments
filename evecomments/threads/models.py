

from evecomments.extensions import db


class ThreadModel(db.Model):
    """ Model for individual sites to be placed in the sites table. """

    __tablename__ = 'threads'

    id    = db.Column(db.String(50), primary_key=True)
    title = db.Column(db.String(50))
    url   = db.Column(db.Integer)

    def __init__(self, thread_id, thread_title, thread_url):
        self.id    = thread_id
        self.title = thread_title
        self.url   = thread_url

    def __repr__(self):
        return '<ThreadModel %s>' % self.id