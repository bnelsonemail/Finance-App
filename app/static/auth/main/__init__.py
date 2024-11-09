"""app / main / __init__.py."""

from flask import Blueprint

# Define the blueprint for the main module
main = Blueprint('main', __name__)

# Import routes to associate them with the blueprint
from . import routes
