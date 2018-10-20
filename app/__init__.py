from flask import Flask

from .auth import auth
def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.Dev")
    app.register_blueprint(auth, url_prefix="/auth")
    return app