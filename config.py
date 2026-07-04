# config.py
import os


def _require_secret(name, fallback):
  """Read a secret from the environment, falling back only outside production."""
  return os.getenv(name, fallback)


class Config(object):
  """
  Common configurations shared across every environment.
  """

  API_VERSION = 'v1'

  # Secrets are read from the environment so they are never committed to source.
  SECRET_KEY = _require_secret('SECRET_KEY', 'dev-only-change-me')
  JWT_SECRET_KEY = _require_secret('JWT_SECRET_KEY', SECRET_KEY)

  SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
  """
  Development configurations.
  """

  DEBUG = True
  SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
  """
  Production configurations.
  """

  DEBUG = False


class TestingConfig(Config):
  """
  Testing configurations backed by an in-memory database.
  """

  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
  SECRET_KEY = 'testing-secret-key-that-is-long-enough-32b'
  JWT_SECRET_KEY = 'testing-secret-key-that-is-long-enough-32b'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
