# Library Management System - Django

A simple Django + SQLite Library Management System based on the supplied flow diagram.

## Features

- Home page
- User signup
- Secure Django password authentication
- Login/logout using Django sessions
- Library dashboard
- Issue a book
- Save book issue data in SQLite
- Book issue success page
- View all issued books
- Django admin panel

## Setup on Windows

Open the project folder in VS Code terminal:

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

Open:

http://127.0.0.1:8000/

## Optional admin

Create an admin account:

```bash
py manage.py createsuperuser
```

Then visit:

http://127.0.0.1:8000/admin/

## Main URLs

- `/` Home
- `/signup/` Sign Up
- `/login/` Login
- `/dashboard/` Dashboard
- `/issue-book/` Issue Book
- `/books/` View Books
- `/logout/` Logout
- `/admin/` Django Admin
