from app import create_app
from app.extensions import db
from sqlalchemy import text

app = create_app()

with app.app_context():
    print("Database URI:", app.config["SQLALCHEMY_DATABASE_URI"])

    tables = db.session.execute(
        text("SELECT name FROM sqlite_master WHERE type='table'")
    ).fetchall()

    print("Tables:", tables)

    version = db.session.execute(
        text("SELECT * FROM alembic_version")
    ).fetchall()

    print("Alembic:", version)