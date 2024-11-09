"""app / budget / routes.py."""

from flask import render_template, request, redirect, url_for, flash
from . import budget  # Import the budget blueprint
from app.models import Budget  # Import your Budget model if it exists
from app import db  # Import the database instance


@budget.route('/overview')
def budget_overview():
    """
    Display an overview of the user's budget.

    Returns:
        Rendered template for the budget overview page,
        displaying all budget entries.
    """
    budgets = Budget.query.all()  # Retrieve all budget entries from the database
    return render_template('budget/budget_overview.html', budgets=budgets)


@budget.route('/add', methods=['GET', 'POST'])
def add_budget():
    """
    Handle adding a new budget entry.

    GET: Render the form for adding a new budget entry.
    POST: Process the form data to create a new budget entry.

    Returns:
        Redirects to the budget overview page on success,
        or re-renders the form on failure.
    """
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        try:
            new_budget = Budget(name=name, amount=amount)
            db.session.add(new_budget)
            db.session.commit()
            flash('Budget entry added successfully!', 'success')
            return redirect(url_for('budget.budget_overview'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding budget entry: {e}', 'error')

    return render_template('budget/add_budget.html')


@budget.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_budget(id):
    """
    Handle editing an existing budget entry.

    GET: Render the form populated with the existing budget data.
    POST: Process the form data to update the budget entry.

    Args:
        id (int): ID of the budget entry to edit.

    Returns:
        Redirects to the budget overview page on success,
        or re-renders the form on failure.
    """
    budget_entry = Budget.query.get_or_404(id)
    if request.method == 'POST':
        budget_entry.name = request.form['name']
        budget_entry.amount = request.form['amount']
        try:
            db.session.commit()
            flash('Budget entry updated successfully!', 'success')
            return redirect(url_for('budget.budget_overview'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating budget entry: {e}', 'error')

    return render_template('budget/edit_budget.html', budget=budget_entry)


@budget.route('/delete/<int:id>', methods=['POST'])
def delete_budget(id):
    """
    Handle deleting an existing budget entry.

    Args:
        id (int): ID of the budget entry to delete.

    Returns:
        Redirects to the budget overview page on success.
    """
    budget_entry = Budget.query.get_or_404(id)
    try:
        db.session.delete(budget_entry)
        db.session.commit()
        flash('Budget entry deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting budget entry: {e}', 'error')

    return redirect(url_for('budget.budget_overview'))
