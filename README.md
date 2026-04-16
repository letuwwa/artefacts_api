# Artefacts API

Django REST API for managing artefacts and archeologists.

## Requirements

- Python 3.12+
- PostgreSQL
- uv

## Setup

Install dependencies:

```bash
uv sync
```

Create a `.env` file in the project root:

```dotenv
SECRET_KEY=YOUR_SECRET_KEY
DB_NAME=DATABASE_NAME
DB_USER=DATABASE_USER_NAME
DB_PASS=DATABASE_USER_PASSWORD
```

Run database migrations:

```bash
uv run python manage.py migrate
```

Start the development server:

```bash
uv run python manage.py runserver
```

The API schema is available at:

- `http://127.0.0.1:8000/doc/`
- `http://127.0.0.1:8000/redoc/`

## Common Commands

```bash
make migrate
make start
```

Format the code:

```bash
uv run black .
```
