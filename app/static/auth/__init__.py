"""app / auth / __init__.py."""

from flask import Blueprint

# Define the blueprint for the auth module
auth = Blueprint('auth', __name__)

# Import routes to associate them with the blueprint
from . import routes
