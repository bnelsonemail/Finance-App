# Project Documentation: Budget and Debt Management App

## Table of Contents
- [Project Documentation: Budget and Debt Management App](#project-documentation-budget-and-debt-management-app)
  - [Table of Contents](#table-of-contents)
  - [Project Scope](#project-scope)
    - [Technologies](#technologies)
  - [High-Level Architecture](#high-level-architecture)

---

## Project Scope

The Budget and Debt Management App aims to help users manage their budgets, track expenses, and work towards debt repayment goals. The application includes:
1. **User Authentication**: Using Auth0 for secure registration, login, and session management.
2. **Dashboard**: A summary of budgets, expenses, income, and debt repayment progress.
3. **Budget Tracker**: Allows users to define expense categories, track totals, and monitor expenses.
4. **Debt Payoff Tool**: Implements the snowball method to help users prioritize debts, make payments, and calculate payoff dates.

### Technologies
- **Backend**: Flask, Flask-SQLAlchemy for ORM, Flask-Migrate for migrations.
- **Authentication**: Auth0 for secure OAuth-based authentication.
- **Database**: SQLite (or any SQL database, adjustable for production).
- **Frontend**: HTML/CSS with Jinja templates for dynamic rendering.
- **APIs and Libraries**: Auth0 API for authentication, authlib for OAuth integration.

---

## High-Level Architecture

The project is structured into modules, each handling specific functionalities.

