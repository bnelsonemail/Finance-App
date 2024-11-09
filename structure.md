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
│   │   └── debt/
│   │       └── debt_calculator.html
│   ├── static/
│       ├── css/
│       ├── js/
│       └── images/
├── migrations/
└── venv/

