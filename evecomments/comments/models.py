

from evecomments.extensions import db


class CommentModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<Comment %s>' % self.id