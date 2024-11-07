"""Models."""

from app import db


class User(db.Model):
    """
    Represents a user in the application.

    Attributes
    ----------
    id : int
        The primary key of the user.
    username : str
        The username of the user.
    email : str
        The email address of the user.
    auth0_id : str
        The Auth0 unique identifier for the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    auth0_id = db.Column(db.String(128), unique=True, nullable=False)


class Budget(db.Model):
    """
    Represents a budget category for the user.

    Attributes
    ----------
    id : int
        The primary key of the budget.
    user_id : int
        Foreign key to associate the budget with a user.
    category : str
        The budget category.
    amount : float
        The allocated budget amount.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(64), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    user = db.relationship('User', backref='budgets')


class Debt(db.Model):
    """
    Represents a debt item for the user.

    Attributes
    ----------
    id : int
        The primary key of the debt.
    user_id : int
        Foreign key to associate the debt with a user.
    name : str
        The name of the debt.
    balance : float
        The current balance of the debt.
    apr : float
        Annual percentage rate for the debt.
    minimum_payment : float
        Minimum monthly payment for the debt.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    apr = db.Column(db.Float, nullable=False)
    minimum_payment = db.Column(db.Float, nullable=False)
    user = db.relationship('User', backref='debts')
