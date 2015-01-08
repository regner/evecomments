""" Each extension is initialized in the application factory. """

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask.ext.restful import Api
from flask.ext.restful.utils.cors import crossdomain
api = Api(decorators=[crossdomain(origin='*')])

from flask.ext.login         import LoginManager
login_manager = LoginManager()

from flask_oauthlib.client import OAuth
oauth  = OAuth()