# Flask and other third party packages
from flask import Flask
from flask_jwt_extended import JWTManager

# App stuff
from app.config import Config
from app.resources import auth_blueprint, health_blueprint


def create_app():
    app = Flask(__name__)
    jwt = JWTManager()

    app.config.from_object(Config)
    jwt.init_app(app)

    app.register_blueprint(health_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
