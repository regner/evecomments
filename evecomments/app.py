

from flask import Flask, redirect, url_for

from evecomments.settings   import DevConfig
from evecomments.extensions import db, api, oauth, login_manager

# Import views for registering their blueprints
from evecomments.comments   import views as comments_views
from evecomments.public     import views as public_views
from evecomments.sites      import views as sites_views
from evecomments.user       import views as user_views


def create_app(config_object=DevConfig):
    """ EVEComments application factory. """

    app = Flask(__name__)
    app.config.from_object(config_object)

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


def register_blueprints(app):
    """ Registers all relevant blueprints for the application """

    app.register_blueprint(comments_views.blueprint)
    app.register_blueprint(public_views.blueprint)
    app.register_blueprint(sites_views.blueprint)
    app.register_blueprint(user_views.blueprint)

    return None


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('user.login'))