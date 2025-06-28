Invoice Management API

A Django REST Framework project for managing invoices, clients, payments, and items.

Features

- CRUD operations for Invoices, Clients, Payments, and Items.
- JWT Authentication for secure API access.
- Filtering and pagination support.
- Admin interface to manage data easily.

Installation

1. Clone the repo:
bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo


2. Create and activate a virtual environment:
bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


3. Install dependencies:
bash
pip install -r requirements.txt


4. Apply migrations:
bash
python manage.py migrate


5. Create a superuser (for admin):
bash
python manage.py createsuperuser


6. Run the development server:
bash
python manage.py runserver
```

