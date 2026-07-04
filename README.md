# Flask API

A sample project that builds a RESTful API using Python and Flask, structured in
clean layers: `controller` (HTTP) -> `service` (business logic) -> `repository`
(data access) -> `model` (persistence), with `schema` handling (de)serialization
and validation.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Secrets are read from environment variables and are never committed to source:

```bash
export SECRET_KEY="a-long-random-string"
export JWT_SECRET_KEY="another-long-random-string"
```

For the database, copy `instance/config.sample.py` to `instance/config.py` and set
`SQLALCHEMY_DATABASE_URI`.

## Getting Started

1. Configure the database (see above).

1. Migrate the database:

   ```bash
   flask db upgrade
   ```

1. Start the Flask application in development mode:

   ```bash
   export FLASK_CONFIG=development
   export FLASK_APP=run.py
   flask run
   ```

## API

| Method | Path            | Auth | Description                    |
|--------|-----------------|------|--------------------------------|
| GET    | `/ping`         | no   | Health check                   |
| POST   | `/v1/user`      | no   | Register a user                |
| GET    | `/v1/user`      | JWT  | List users (paginated)         |
| POST   | `/v1/auth`      | no   | Log in, returns JWT tokens     |
| GET    | `/v1/type`      | no   | List types (paginated)         |
| POST   | `/v1/type`      | no   | Create a type                  |
| GET    | `/v1/type/<id>` | no   | Get a type by id               |
| PUT    | `/v1/type/<id>` | no   | Update a type                  |

Request and response bodies use `snake_case` fields (for example `{"name": "..."}`).
List endpoints accept `page_size` and `page_position` query parameters and return a
`Data`/`Meta` envelope.

## Running Tests

```bash
python -m pytest
```

The suite runs against an in-memory SQLite database (the `testing` config), so no
external database is required.
