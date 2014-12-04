

from flask.ext.restful import Resource

from evecomments.extensions      import db
from evecomments.comments.models import CommentModel


class Comment(Resource):
    """ Resource for a single comment. """

    def get(self):
        """ Returns a single comment. """

        test_comment = CommentModel()
        db.session.add(test_comment)
        db.session.commit()

        return {}


def register_resources(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """

    api.add_resource(Comment, '/api/comments/', endpoint='comment')