"""app / budget / __init__.py."""

from flask import Flask
from .budget import budget as budget_blueprint


def create_app():
    app = Flask(__name__)
    
    # Register the budget blueprint with a URL prefix
    app.register_blueprint(budget_blueprint, url_prefix='/budget')

    # Register other blueprints or configure the app as needed

    return app
