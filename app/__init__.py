"""App / __init__.py."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    """
    Factory function to create and configure the Flask application.

    Parameters
    ----------
    config_class : class
        The configuration class to initialize the app with.

    Returns
    -------
    app : Flask
        The configured Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app
