

from evecomments.extensions import db


class CommentModel(db.Model):
    """ Model for individual comments to be placed in the comments table. """

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Comment %s>' % self.id