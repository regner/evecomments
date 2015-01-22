

from flask.ext.restful import Resource, reqparse, abort

from evecomments.extensions      import db
from evecomments.user.models     import UserModel
from evecomments.sites.models    import SiteModel
from evecomments.comments.models import CommentModel


def format_comment_v1(comment):
    """ Takes a single CommentModel object and formats it into a V1 API response """

    formatted_response = {
        'id'                 : comment.id,
        'site_id'            : comment.site_id,
        'message'            : comment.message,
        'created_on'         : comment.created_on.isoformat(),
        'parent_comment_id'  : comment.parent_comment_id,
        'author_id'          : comment.author_id,
        'author_name'        : comment.author.name,
        'author_image_links' : comment.author.get_image_server_links()
    }

    return formatted_response


class CommentV1(Resource):
    """ Resource for a single comment. """

    def get(self, site_id, comment_id):
        """ Returns a single comment. """

        # Start by fetching the site specified
        site = SiteModel.query.filter_by(id=site_id).first()

        # We don't actually need the site object, we just want to make sure it exists
        # We want to abort on the missing site rather than return 0 comments if the site doesn't exist
        if site is None:
            abort(404, message='Site {} does not exist.'.format(site_id))

        comment = CommentModel.query.filter_by(site_id=site_id, id=comment_id).first()
        if comment is None:
            abort(404, message='Comment {} does not exist.'.format(comment_id))

        return format_comment_v1(comment)


class CommentCollectionV1(Resource):
    """ Resource for getting all comments and creating new ones. """

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('message', type=str, required=True,  location='json')
        self.reqparse.add_argument('parent',  type=int, required=False, location='json')

        super(CommentCollectionV1, self).__init__()

    def get(self, site_id):
        """ Returns a list of all comments. """

        # Start by fetching the site specified
        site = SiteModel.query.filter_by(id=site_id).first()

        # We don't actually need the site object, we just want to make sure it exists
        # We want to abort on the missing site rather than return 0 comments if the site doesn't exist
        if site is None:
            abort(404, message='Site {} does not exist.'.format(site_id))

        # Fetch and format the comments for the specified site
        comments           = CommentModel.query.filter_by(site_id=site_id).all()
        formatted_comments = [format_comment_v1(comment) for comment in comments]

        return formatted_comments

    def post(self, site_id):
        """ Creates a new comment. """

        # Start by fetching the site the comment is for
        site = SiteModel.query.filter_by(id=site_id).first()

        if site is None:
            abort(404, message='Site {} does not exist.'.format(site_id))

        # Parse the request data and confirm required fields are there
        args = self.reqparse.parse_args()

        # Until we have user auth working again assume CCP FoxFour (92168909)
        user = UserModel.query.filter_by(id=92168909).first()

        # Create a new comment
        new_comment = CommentModel(site, args['message'], user)

        # Deal with the parent comment if one is specified
        if 'parent' in args and args['parent'] is not None:
            parent = CommentModel.query.filter_by(id=args['parent']).first()

            if parent is None:
                abort(404, message='Parent comment {} does not exist.'.format(args['parent']))

            new_comment.parent = parent

        # Save the new comment to the db! :D
        db.session.add(new_comment)
        db.session.commit()

        return format_comment_v1(new_comment)


def register_resources(api):
    """ Registers the API resources defined in this file with the app in it's application factory. """

    api.add_resource(CommentCollectionV1, '/api/v1/comments/<int:site_id>',                  endpoint='comments')
    api.add_resource(CommentV1,           '/api/v1/comments/<int:site_id>/<int:comment_id>', endpoint='comment')