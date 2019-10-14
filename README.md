# Flask API
A sample project to built Restful API using python and flask

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies

```bash
pip install -r requirements.txt
```

## Getting Started

### Manual Setup

1. Make a config file by copying the configuration sample in `./instance/config.py.sample` to `./instance/config,py`

1. Modify the database configuration in `./instance/config.py`

1. Migrate the database by running the following command

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

1. Start Flask application in development mode

   ```cmd
   :: For Windows
   set flask_config=development
   set flask_env=development
   set flask_app=run.py
   flask run
   ```

   ```bash
   # For Linux/UNIX Shell
   export flask_config=development
   export flask_env=development
   export flask_app=run.py
   flask run
   ```

### Automatic Setup (for Debian-based Linux; incl. Ubuntu and WSL)

Coming Soon.
