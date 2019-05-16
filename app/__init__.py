# third-party imports
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

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
  
  # db initialization
  db.init_app(app)
  
  # db migration initialization
  migrate = Migrate(app, db)

  # API initialization
  api = Api(app)

  # CORS
  CORS(app)

  # routes initialization
  from app.routes import routes
  routes(app, api)

  @app.route('/')
  def main():
    return 'page not found'

  return app