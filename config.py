class Config:

    SECRET_KEY = "your-secret-key"


class DevelopmentConfig(Config):

    DEBUG = True


class ProductionConfig(Config):

    DEBUG = False

    