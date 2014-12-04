

from flask.ext.restful import Resource, reqparse, fields, marshal, abort

from evecomments.extensions      import db
from evecomments.comments.models import CommentModel


comment_fields = {
    'id' : fields.Integer,
}


class Comment(Resource):
    """ Resource for a single comment. """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('comment_id', type=int, required=True, location='json')

        super(Comment, self).__init__()

    def get(self, comment_id):
        """ Returns a single comment. """

        data = CommentModel.query.filter_by(id=comment_id).first()

        if data is None:
            abort(404, message='Comment {} does not exist.'.format(comment_id))

        return marshal(data, comment_fields)


class Comments(Resource):
    """ Resource for getting all comments and creating new ones. """

    def get(self):
        """ Returns a list of all comments. """

        data = CommentModel.query.all()

        return marshal(data, comment_fields)

    def post(self):
        """ Creates a new comment. """

        test_comment = CommentModel()
        db.session.add(test_comment)
        db.session.commit()

        return marshal(test_comment, comment_fields)


def register_resources(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """

    api.add_resource(Comments, '/api/comments/',                  endpoint='comments')
    api.add_resource(Comment,  '/api/comments/<int:comment_id>/', endpoint='comment')