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

# SQLAlchemy and Marshamllow Initialization
db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_name):
  app = Flask(__name__, instance_relative_config=True)

  # get config
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.secret_key = app.config['SECRET_KEY']

  # strict slashes
  app.url_map.strict_slashes = False
  
  # db initialization
  db.init_app(app)
  
  # db migration initialization
  migrate = Migrate(app, db)

  # API initialization
  api = Api(app)

  # CORS
  CORS(app)

  # jwt initialization
  jwt = JWTManager(app)
  
  # routes initialization
  from app.routes import routes
  routes(app, api)

  @app.errorhandler(404)
  def notFound(e):
    return 'page not found', 404

  @app.before_request
  def clear_trailing():
    from flask import redirect, request
    rp = request.path 
    if rp != '/' and rp.endswith('/'):
      return redirect(rp[:-1])

  return app