

from flask import Flask

from evecomments.settings   import DevConfig
from evecomments.extensions import db, api, oauth, login_manager

# Import views for registering their blueprints
from evecomments.public     import views as public_views
from evecomments.sites      import views as sites_views
from evecomments.embed      import views as embed_views

# Import APIs for registering their resources
from evecomments.comments   import api as comments_api


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

    db.init_app(app)
    api.init_app(app)
    oauth.init_app(app)
    login_manager.init_app(app)

    return None


def register_resources():
    """ Registers all Flask-RESTful resources. """

    comments_api.register_resources(api)

    return None


def register_blueprints(app):
    """ Registers all relevant blueprints for the application """

    app.register_blueprint(public_views.blueprint)
    app.register_blueprint(sites_views.blueprint)
    app.register_blueprint(embed_views.blueprint)

    return None