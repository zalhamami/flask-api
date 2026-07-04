import os

# third-party imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# local imports
from config import app_config

# Extension singletons, bound to the app inside the factory.
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
jwt = JWTManager()


def create_app(config_name=None):
  config_name = config_name or os.getenv('FLASK_CONFIG', 'development')

  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py', silent=True)
  app.secret_key = app.config['SECRET_KEY']

  # A single, consistent trailing-slash policy (no manual redirects).
  app.url_map.strict_slashes = False

  db.init_app(app)
  migrate.init_app(app, db)
  ma.init_app(app)
  CORS(app)
  jwt.init_app(app)

  api = Api(app)

  from app.routes import routes
  routes(app, api)

  register_error_handlers(app)

  return app


def register_error_handlers(app):
  @app.errorhandler(404)
  def not_found(error):
    return {'code': 404, 'message': 'resource not found'}, 404

  @app.errorhandler(500)
  def server_error(error):
    return {'code': 500, 'message': 'internal server error'}, 500
