

from eve_utils.image_server import get_image_server_link

from evecomments.extensions import db


class UserModel(db.Model):
    """ Model for users. """

    __tablename__ = 'users'

    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(length=128))
    hash        = db.Column(db.String(length=256))
    join_date   = db.Column(db.DateTime)
    login_count = db.Column(db.Integer)

    def __init__(self, character_id, character_name, character_hash):
        self.id   = character_id
        self.name = character_name
        self.hash = character_hash

    def __repr__(self):
        return '<UserModel %s>' % self.id

    # Flask-Login integration
    @staticmethod
    def is_authenticated():
        return True

    # Flask-Login integration
    @staticmethod
    def is_active():
        return True

    # Flask-Login integration
    @staticmethod
    def is_anonymous():
        return False

    # Flask-Login integration
    def get_id(self):
        return self.id

    def get_image_server_link(self, icon_size=128):
        return get_image_server_link(self.id, 'char', icon_size)