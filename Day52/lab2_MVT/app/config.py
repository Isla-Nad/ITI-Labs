import os


class Config:
    SECRET_KEY = os.urandom(32)

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.sqlite"


class ProductionConfig(Config):
    DEBUG = False
    # postgresql://username:password@localhost:portnumber/dbname
    SQLALCHEMY_DATABASE_URI = "postgresql://test:test@localhost:5432/flask"


projectConfig = {
    "dev": DevelopmentConfig,
    'prd': ProductionConfig
}
