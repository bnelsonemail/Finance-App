BudgetApp/
│
├── .env                     # Environment variables
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── templates/
│   │   └── layout.html
│   ├── static/
├── config.py
├── migrations/
    ├── README
    ├── env.py
    ├── alembic.ini
    ├── script.py.mako
    └── versions/
        ├── 3b1d3b98ef4a_add_users_table.py
        ├── 4c2d3c98cf5b_add_budgets_table.py
        └── 6e4f8d90df2c_add_debt_table.py
├── run.py
└── venv/                    # Virtual environment
