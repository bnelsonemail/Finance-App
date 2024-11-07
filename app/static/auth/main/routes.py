from flask import Blueprint, render_template
from app.auth.routes import requires_auth

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('layout.html')


@main.route('/dashboard')
@requires_auth
def dashboard():
    return 'Welcome to your dashboard!'
