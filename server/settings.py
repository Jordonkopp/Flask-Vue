import os

class Config:
    SECRET_KEY = "testkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "api.log"


class DevelopmentConfig(Config):
    os.getenv('FLASK_DEBUG')
    SQLALCHEMY_DATABASE_URI = "postgres://testusr:password@127.0.0.1:5432/testdb"
    DEBUG = True


class ProductionConfig(Config):
    HOST = os.environ.get("DATABASE_URL")
    USER = os.environ.get("DB_USER")
    PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (USER, PASS, HOST, 5432, DB_NAME)
    DEBUG = False


class DockerDevConfig(Config):
    HOST = os.environ.get("DATABASE_URL")
    USER = os.environ.get("DB_USER")
    PASS = os.environ.get("DB_PASS")
    DB_NAME = os.environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = 'postgres://%s:%s@%s:%s/%s' % (USER, PASS, HOST, 5432, DB_NAME)
    DEBUG = True


config = {"dev": DevelopmentConfig, "prod": ProductionConfig, "docker": DockerDevConfig}
