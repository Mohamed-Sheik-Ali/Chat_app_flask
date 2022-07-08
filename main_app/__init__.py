from flask import Flask

from .core.extensions import mongo

from .core.routes import core


def create_app(config_file='settings.py'):

    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://sheik123:root123@cluster0.jjjfkbi.mongodb.net/mydb?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.config.from_pyfile(config_file)

    app.register_blueprint(core)

    return app
