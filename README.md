# Note Taker (Flask)

A small Flask-based note taking web app. This repository contains the server, views, and templates used to create, view, and manage notes with user authentication.

## Features

- User registration and login
- Create and delete notes
- Simple HTML templates using Jinja2
- SQLite/SQLAlchemy integration (configurable)

## Quick Start

The repo includes a virtual environment at `ecom/` (optional). If you prefer a fresh environment, create one first.

1. Activate the included virtual environment (optional):

```bash
source ecom/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

You can run the app directly with Python or using the Flask CLI.

Directly with Python:

```bash
python main.py
```

Open `http://127.0.0.1:5000` in your browser.

## Project layout

- `main.py` — application entrypoint
- `website/` — Flask package: `__init__.py`, `views.py`, `models.py`, `auth.py`
- `templates/` — Jinja2 templates (login, signup, home)
- `static/` — static assets (JS, CSS)
- `instance/` — instance folder for config and DB (not committed)

## Configuration

- Database and secret keys can be configured via environment variables or the `instance/` folder.
- The app uses `Flask-Login` and `Flask-SQLAlchemy` (see `requirements.txt`).


