import os
import sys

# 1. FORCE the environment variables BEFORE importing app or db
os.environ["FLASK_ENV"] = "testing"
os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"




import pytest
from app import create_app, db
from app.user_repo import create_user

@pytest.fixture
def app():
    app = create_app(config={"TESTING":True, "SQLALCHEMY_DATABASE_URI":"sqlite:///test.db"})

    with app.app_context():
        db.create_all()

        yield app

        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def user(app):
    user = create_user(
        username="emodoh",
        email="emodoh@test.com",
        password="4199"
    )
    return user