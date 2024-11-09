"""app / auth / routes.py."""

import os
from flask import Blueprint, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
from app import db
from app.models import User
from finance_app import config



# Load environment variables
load_dotenv()

auth_bp = Blueprint('auth', __name__)
oauth = OAuth()

# Auth0 configuration
oauth.register(
    AUTH0_DOMAIN=os.getenv("AUTH0_DOMAIN"),
    AUTH0_CLIENT_ID=os.getenv("AUTH0_CLIENT_ID"),
    AUTH0_CLIENT_SECRET=os.getenv("AUTH0_CLIENT_SECRET"),
    AUTH0_AUDIENCE=os.getenv("AUTH0_AUDIENCE"),
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


def get_auth0_token():
    """
    Retrieves an access token from Auth0 using the Client Credentials Grant.

    Returns
    -------
    str
        The access token if successful, or None if authentication fails.
    """
    url = f"https://{AUTH0_DOMAIN}/oauth/token"
    headers = {"content-type": "application/json"}
    payload = {
        "client_id": AUTH0_CLIENT_ID,
        "client_secret": AUTH0_CLIENT_SECRET,
        "audience": AUTH0_AUDIENCE,
        "grant_type": "client_credentials"
    }

    try:
        # Make the POST request to Auth0
        response = requests.post(url, json=payload, headers=headers)

        # Raise an error for HTTP status codes 4xx/5xx
        response.raise_for_status()

        # Parse the JSON response and retrieve the access token
        token = response.json().get("access_token")
        if token:
            print("Access token retrieved successfully.")
            return token
        else:
            # Handle unexpected response format
            print("Error: Access token not found in response.")
            return None

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - {response.json()}")
    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except Timeout as timeout_err:
        print(f"Request timed out: {timeout_err}")
    except RequestException as req_err:
        print(f"An error occurred with the request: {req_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    return None


# Example usage of the token retrieval
token = get_auth0_token()
if token:
    print("Your Auth0 Access Token:", token)
