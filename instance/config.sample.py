# Copy this file to instance/config.py and adjust for your environment.
# Secrets (SECRET_KEY / JWT_SECRET_KEY) are read from environment variables by
# default (see config.py); only override them here if you are not using env vars.

SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/database_name'
# SECRET_KEY = 'change-me'
# JWT_SECRET_KEY = 'change-me'
