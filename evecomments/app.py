

from flask import Flask

from evecomments.settings     import DevConfig
from evecomments.extensions   import api, login_manager
from evecomments.public.views import blueprint as public_blueprint


def create_app(config_object=DevConfig):
    """ EVEComments application factory. """

    app = Flask(__name__)
    app.config.from_object(config_object)

    register_resources()
    register_blueprints(app)
    register_extensions(app)

    return app


def register_extensions(app):
    """ Registers all relevant extensions. """

    api.init_app(app)
    login_manager.init_app(app)

    return None


def register_resources():
    """ Registers all Flask-RESTful resources. """

    #map.register_resources(api)

    return None


def register_blueprints(app):
    """ Registers all relevant blueprints for the application """

    app.register_blueprint(public_blueprint)

    return None