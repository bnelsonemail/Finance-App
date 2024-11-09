"""app / debt / routes.py."""

from flask import render_template, request, redirect, url_for, flash
from app.models import Debt  # Import your Debt model if it exists
from app import db  # Import the database instance
from . import debt  # Import the debt blueprint


@debt.route('/overview')
def debt_overview():
    """
    Display an overview of the user's debts.

    Returns:
        Rendered template for the debt overview page, displaying all debt
        entries.
    """
    debts = Debt.query.all()  # Retrieve all debt entries from the database
    return render_template('debt/debt_overview.html', debts=debts)


@debt.route('/add', methods=['GET', 'POST'])
def add_debt():
    """
    Handle adding a new debt entry.

    GET: Render the form for adding a new debt entry.
    POST: Process the form data to create a new debt entry.

    Returns:
        Redirects to the debt overview page on success, or re-renders the
        form on failure.
    """
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        interest_rate = request.form['interest_rate']
        try:
            new_debt = Debt(name=name, amount=amount,
                            interest_rate=interest_rate)
            db.session.add(new_debt)
            db.session.commit()
            flash('Debt entry added successfully!', 'success')
            return redirect(url_for('debt.debt_overview'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding debt entry: {e}', 'error')

    return render_template('debt/add_debt.html')


@debt.route('/calculate/<int:id>', methods=['GET'])
def calculate_payoff(id):
    """
    Calculate the payoff schedule for a specific debt.

    Args:
        id (int): ID of the debt entry to calculate payoff for.

    Returns:
        Rendered template displaying the payoff schedule.
    """
    debt_entry = Debt.query.get_or_404(id)
    payoff_schedule = calculate_debt_payoff(debt_entry)
    return render_template(
        'debt/debt_payoff.html', debt=debt_entry, schedule=payoff_schedule
    )


@debt.route('/delete/<int:id>', methods=['POST'])
def delete_debt(id):
    """
    Handle deleting an existing debt entry.

    Args:
        id (int): ID of the debt entry to delete.

    Returns:
        Redirects to the debt overview page on success.
    """
    debt_entry = Debt.query.get_or_404(id)
    try:
        db.session.delete(debt_entry)
        db.session.commit()
        flash('Debt entry deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting debt entry: {e}', 'error')

    return redirect(url_for('debt.debt_overview'))


def calculate_debt_payoff(debt):
    """
    Calculate a payoff schedule for a given debt entry.

    Args:
        debt (Debt): Debt instance to calculate payoff for.

    Returns:
        list: Payoff schedule containing payment dates and remaining balance.
    """
    # Placeholder logic for debt payoff calculation
    # Replace this with actual calculation logic as needed
    schedule = [
        {"month": 1, "balance": debt.amount * 0.9},
        {"month": 2, "balance": debt.amount * 0.8},
        {"month": 3, "balance": debt.amount * 0.7},
    ]
    return schedule
