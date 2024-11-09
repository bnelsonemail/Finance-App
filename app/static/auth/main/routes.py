"""app / main / routes.py."""

from flask import Blueprint, render_template
from app.auth.routes import requires_auth

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """
    Render the index page.

    This route renders the 'layout.html' template, which serves as the
    main landing page for the application.

    Returns:
        Rendered HTML template for the index page.
    """
    return render_template('layout.html')


@main.route('/dashboard')
@requires_auth
def dashboard():
    """
    Render the dashboard page, accessible only to authenticated users.

    This route requires user authentication. If the user is authenticated,
    it returns a welcome message indicating access to the dashboard.

    Returns:
        str: A welcome message for authenticated users.
    """
    return 'Welcome to your dashboard!'
