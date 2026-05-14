# Django Blog Project

A fully functional blog website developed using Django. This project allows users to create, update, manage, and interact with blog posts through a modern and responsive interface.

---

# Features

- User Registration and Login System
- Create, Update, and Delete Blog Posts
- User Profile Management
- Comment System
- Image Upload Functionality
- Responsive Design
- Authentication and Authorization
- Admin Panel for Content Management

---

# Technologies Used

- Python
- Django
- HTML5
- CSS3
- SQLite3
- Pillow

---

# Project Folder Structure

```bash
DJANGO_BLOG_PROJECT/
│
├── blogsite/
│   │
│   ├── blogapp/
│   │   ├── migrations/
│   │   ├── static/
│   │   │   └── blog/
│   │   │       └── style.css
│   │   │
│   │   ├── templates/
│   │   │   ├── blog/
│   │   │   │   ├── create_post.html
│   │   │   │   ├── delete_post.html
│   │   │   │   ├── edit_profile.html
│   │   │   │   ├── home.html
│   │   │   │   ├── post_detail.html
│   │   │   │   ├── profile.html
│   │   │   │   ├── register.html
│   │   │   │   └── update_post.html
│   │   │   │
│   │   │   └── registration/
│   │   │       ├── login.html
│   │   │       └── logout.html
│   │   │
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── blogsite/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── media/
│   │   └── post_images/
│   │
│   ├── db.sqlite3
│   └── manage.py
```

---

# Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/Karina-p1/django-blog-project.git
```

## 2. Move into the Project Directory

```bash
cd django-blog-project
```

## 3. Create Virtual Environment

### Mac/Linux

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Windows

```bash
python -m venv myenv
myenv\Scripts\activate
```

---

# Install Required Packages

```bash
pip install django
pip install pillow
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

# Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Create Admin User

```bash
python manage.py createsuperuser
```

---

# Run the Development Server

```bash
python manage.py runserver
```

Open the project in your browser:

```bash
http://127.0.0.1:8000/
```

---

# Main Pages

- Home Page
- User Registration Page
- Login & Logout Page
- Create Blog Post Page
- Update/Delete Blog Post Page
- Profile Page
- Post Detail Page

---

# Future Enhancements

- Search Functionality
- Blog Categories
- Like and Share System
- REST API Integration
- Dark Mode UI
- Email Verification

---

# Learning Outcomes

This project demonstrates:

- Django Models and ORM
- CRUD Operations
- Authentication System
- Form Handling
- Media Uploads
- URL Routing
- Template Rendering
- Static and Media Files Handling

---

# Author

Karina Paudel

GitHub Repository:  
https://github.com/Karina-p1/django-blog-project
