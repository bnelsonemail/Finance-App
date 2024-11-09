finance_app/
├── .env
├── config.py
├── run.py
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── budget/                     # New budget blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── services.py             # Service layer for budget logic
│   ├── debt/                       # New debt blueprint
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── calculator.py           # Debt payoff calculation logic
│   ├── templates/
│   │   ├── base.html
│   │   ├── layout.html
│   │   ├── dashboard.html
│   │   ├── auth/
│   │   │   └── login.html
│   │   ├── budget/
│   │   │   └── budget_overview.html
│   │   │   ├── budget_overview.html   # Displays a list of all budget entries
│   │   │   ├── add_budget.html        # Form for adding a new budget entry
│   │   │   └── edit_budget.html       # Form for editing an existing budget entry
│   │   └── debt/
│   │       └── debt_calculator.html
│   │       ├── debt_overview.html   # Displays a list of all debt entries
│   │       ├── add_debt.html        # Form for adding a new debt entry
│   │       └── debt_payoff.html     # Displays the debt payoff schedule for a specific debt
│   ├── static/
│       ├── js/
│       └── images/
├── migrations/
└── venv/

