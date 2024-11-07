"""app / auth / routes.py."""

from flask import Blueprint, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from app import db
from app.models import User
from finance_app import config


auth_bp = Blueprint('auth', __name__)
oauth = OAuth()

# Auth0 configuration
oauth.register(
    'auth0',
    client_id=Config.AUTH0_CLIENT_ID,
    client_secret=Config.AUTH0_CLIENT_SECRET,
    client_kwargs={'scope': 'openid profile email'},
    server_metadata_url=f'https://{Config.AUTH0_DOMAIN}/.well-known/openid-configuration',
)


@auth_bp.route('/login')
def login():
    """
    Redirects the user to Auth0 login page.
    """
    return oauth.auth0.authorize_redirect(
        redirect_uri=Config.AUTH0_CALLBACK_URL
    )


@auth_bp.route('/callback')
def callback():
    """
    Handles the callback from Auth0 and logs the user in.
    """
    token = oauth.auth0.authorize_access_token()
    user_info = token['userinfo']

    # Check if user exists; if not, add to database
    user = User.query.filter_by(auth0_id=user_info['sub']).first()
    if not user:
        user = User(
            username=user_info['nickname'],
            email=user_info['email'],
            auth0_id=user_info['sub']
        )
        db.session.add(user)
        db.session.commit()

    session['user'] = user_info
    return redirect(url_for('main.dashboard'))


@auth_bp.route('/logout')
def logout():
    """
    Logs the user out of the application and clears the session.
    """
    session.clear()
    return redirect(
        f'https://{Config.AUTH0_DOMAIN}/v2/logout?client_id='
        f'{Config.AUTH0_CLIENT_ID}&returnTo={url_for("auth.login",_external=True)}'
    )


# Decorator to protect routes
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated
