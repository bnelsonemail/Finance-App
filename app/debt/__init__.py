"""app / debt / __init__.py."""

from flask import Blueprint

# Define the blueprint for the debt module
debt = Blueprint('debt', __name__)

# Import routes to associate them with the blueprint
from . import routes
