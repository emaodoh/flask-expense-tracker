# Flask Expense Tracker

A modern Expense Tracker built with **Python**, **Flask**, **SQLite**, and **SQLAlchemy**.

This project started as a simple expense tracker using JSON storage and has been progressively refactored into a professional Flask application following backend engineering best practices.

---

## Features

* Add new expenses
* View all expenses
* Edit existing expenses
* Delete expenses
* Expense statistics dashboard
* Flash messages for user feedback
* Custom 404 and 500 error pages
* Flask Application Factory
* Blueprints for modular routing
* Service layer for business logic
* Repository layer for database access
* SQLite database
* SQLAlchemy ORM

---

## Tech Stack

### Backend

* Python 3
* Flask
* SQLAlchemy
* SQLite

### Frontend

* HTML5
* CSS3
* Jinja2 Templates

### Development Tools

* Git
* GitHub
* Virtual Environment (venv)

---

## Project Structure

```text
ExpenseTracker/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── services.py
│   ├── expense_repo.py
│   ├── models.py
│   ├── extensions.py
│   └── ...
│
├── static/
├── templates/
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Architecture

The project follows a layered architecture:

```text
Browser
    │
    ▼
Routes (Blueprints)
    │
    ▼
Services (Business Logic)
    │
    ▼
Repository (Database Operations)
    │
    ▼
SQLAlchemy ORM
    │
    ▼
SQLite Database
```

Separating responsibilities in this way keeps the codebase easier to maintain, test, and extend.

---

## Current Progress

### Completed

* Flask application factory
* Blueprints
* Modular project structure
* Expense model
* CRUD operations
* SQLite integration
* SQLAlchemy migration
* Error handling
* Dashboard statistics

### In Progress

* Flask-Migrate
* Authentication
* REST API
* Automated testing

---

## Future Roadmap

### MVP

* Flask-Migrate
* User authentication
* REST API
* Unit testing
* Deployment

### Version 2

* PostgreSQL
* Docker
* AI-powered expense categorization
* Natural language expense entry
* Voice expense recording
* Receipt scanning
* AI spending insights

---

## Installation

Clone the repository:

```bash
git clone https://github.com/emaodoh/flask-expense-tracker.git
```

Navigate into the project:

```bash
cd flask-expense-tracker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

---

## Learning Goals

This project is part of my journey toward becoming a professional backend and AI engineer.

The focus is not only to build a working application but also to understand:

* Software architecture
* Backend engineering principles
* Database design
* REST API development
* Authentication
* Testing
* Deployment
* AI integration

---

## Author

**Emmanuel Odoh**

GitHub: https://github.com/emaodoh

---
