from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR/"expenses.db"

class Config:

    SECRET_KEY = "your-secret-key"
    

class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):

    DEBUG = False

    