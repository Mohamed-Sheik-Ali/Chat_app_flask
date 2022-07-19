from flask import Flask

from .core.extensions import mongo

from .core.routes import core


def create_app(config_file='settings.py'):

    app = Flask(__name__, template_folder='./core/templates')

    app.config['MONGO_URI'] = 'mongodb+srv://venzo:root@cluster0.wwbxdzb.mongodb.net/chat_app?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.config.from_pyfile(config_file)

    app.register_blueprint(core)

    return app
