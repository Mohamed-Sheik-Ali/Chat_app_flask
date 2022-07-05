from flask import Flask

from .core.routes import core

from .core.extensions import mongo


def create_app(config_file='settings.py'):

    app = Flask(__name__)

    app.config['MONGO_URI'] = 'MongoDB URI goes here'

    app.config.from_pyfile(config_file)

    mongo.init_app(app)

    app.register_blueprint(core)

    return app
