

from flask.ext.restful import Resource, reqparse, fields, marshal, abort

from evecomments.extensions      import db
from evecomments.sites.models    import SiteModel
from evecomments.comments.models import CommentModel


comment_fields = {
    'id'      : fields.Integer,
    'site_id' : fields.Integer,
    'message' : fields.String,
    'deleted' : fields.Boolean,
}


class Comment(Resource):
    """ Resource for a single comment. """

    def get(self, site_id, comment_id):
        """ Returns a single comment. """

        data = CommentModel.query.filter_by(id=comment_id).first()
        if data is None:
            abort(404, message='Comment {} does not exist.'.format(comment_id))

        return marshal(data, comment_fields)


class Comments(Resource):
    """ Resource for getting all comments and creating new ones. """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type=str, required=True,  location='json')
        self.reqparse.add_argument('parent',  type=int, required=False, location='json')

        super(Comments, self).__init__()

    def get(self, site_id):
        """ Returns a list of all comments. """

        site = SiteModel.query.filter_by(id=site_id).first()
        if site is None:
            abort(404, message='Site {} does not exist.'.format(site_id))

        comments = CommentModel.query.filter_by(site_id=site_id).all()

        return marshal(comments, comment_fields)

    def post(self, site_id):
        """ Creates a new comment. """

        site = SiteModel.query.filter_by(id=site_id).first()
        if site is None:
            abort(404, message='Site {} does not exist.'.format(site_id))

        args = self.reqparse.parse_args()

        new_comment = CommentModel(site, args['message'])

        if 'parent' in args and args['parent'] is not None:
            parent = CommentModel.query.filter_by(id=args['parent']).first()

            if parent is None:
                abort(404, message='Parent comment {} does not exist.'.format(args['parent']))

            new_comment.parent = parent

        db.session.add(new_comment)
        db.session.commit()

        return marshal(new_comment, comment_fields)


def register_resources(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """

    api.add_resource(Comments, '/api/comments/<int:site_id>/',                  endpoint='comments')
    api.add_resource(Comment,  '/api/comments/<int:site_id>/<int:comment_id>/', endpoint='comment')