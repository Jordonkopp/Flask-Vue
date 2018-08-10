import os
import logging

from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists

from server.settings import config
from server.utils.core_utils import all_exception_handler
from server.models import db

# import blueprints
from server.services.key import key
from server.services.main import main
from server.services.user import user


class Log_Formatter(logging.Formatter):
    def format(self, record):
        record.url = request.url
        record.remote_addr = request.remote_addr
        return super().format(record)


def create_app(test_config=None):
    app = Flask(__name__)

    CORS(app)  # add CORS

    # check environment variables to see which config to load
    env = os.environ.get("FLASK_ENV", "dev")
    if test_config:
        # ignore environment variable config if config was given
        app.config.from_mapping(**test_config)
    else:
        app.config.from_object(config[env])

    # logging
    formatter = Log_Formatter(
        "%(asctime)s %(remote_addr)s: requested %(url)s: %(levelname)s in [%(module)s: %(lineno)d]: %(message)s"
    )

    # Set stream logger
    stream = logging.StreamHandler()
    stream.setLevel(logging.DEBUG)
    stream.setFormatter(formatter)

    app.logger.addHandler(stream)
    app.logger.setLevel(logging.DEBUG)

    # Set Logging to file
    if app.config.get("LOG_FILE"):
        file_handler = logging.FileHandler(app.config.get("LOG_FILE"))
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)

    # if not prod recreate db every-run
    if env != "prod":
        db_url = app.config["SQLALCHEMY_DATABASE_URI"]
        if not database_exists(db_url):
            create_database(db_url)

    # register sqlalchemy to this app
    db.init_app(app)
    Migrate(app, db)

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(key)
    app.register_blueprint(user)


    # register error Handler
    app.register_error_handler(Exception, all_exception_handler)

    return app
