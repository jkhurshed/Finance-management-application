# Finance-management-application
Django rest framework application for managing finances. 
This is a Django Rest Framework application for managing finances. 
It allows users to track their income and expenses, create budgets, and generate reports.

## Features
- User authentication and authorization

- Create, update, and delete income and expense entries

- Create and update wallets

- View reports on income, expenses, and wallet performance

---

## How to start
1) Clone the repository: 
```
git clone https://github.com/jkhurshed/Finance-management-application.git
```
2) Create a virtual environment: 
```
python -m venv .venv
```
3) Activate the virtual environment: 
```
source .venv/bin/activate
```
4) Install dependencies: 
```
pip install -r requirements.txt
```
5) Run migrations: 
```
python manage.py migrate
```
6) Load fixtures:
```
python manage.py loaddata finance_app/wallet
python manage.py loaddata finance_app/category
python manage.py loaddata transaction/transaction
```
7) Run the development server: 
```
python manage.py runserver
```
Open admin panel [localhost:8000](http://localhost:8000/admin)

Default admin: admin

Default password: 123

Open Swagger API documentation [localhost:8000/swagger/](http://localhost:8000/swagger/)

---

## API Endpoints

- /api/v1/transaction/income/: POST requests to create income entries

- /api/v1/transaction/expense/: POST requests create expense entries

- /api/v1/transaction/transactions/: GET request to list transactions

- /api/v1/finance/category/: GET, POST requests to list or create categories

- /api/v1/finance/category/<int:pk>/: GET, PATCH, DELETE requests to retrieve, update, or delete a specific categories

- /api/v1/finance/wallet/: GET, POST requests to list or create wallet

- /api/v1/finance/wallet/<int:pk>/: GET, PATCH, DELETE requests to retrieve, update, or delete a specific wallet
