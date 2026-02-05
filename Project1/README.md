# Project 1: Django Web Application

This project demonstrates building a web application using Django.

## Installation

1. Install uv and Django:
   ```
   pip install uv
   uv venv
   .venv\Scripts\activate
   uv pip install django
   ```

## Creating Project Dependency

```
django-admin startproject mysite projectname
```

## Run Server

```
python manage.py runserver
python manage.py migrate
```

## Create New App

```
python manage.py startapp polls
```

## Today's Work

- Utilized `python manage.py shell` command for interactive testing and data manipulation in the Django shell.
- Created register and login pages with corresponding HTML templates (register.html and login.html) for user authentication.
- Developed a User model in polls/models.py with fields for first_name, last_name, and email.
- Implemented a user list view in polls/views.py to display all users using the user_list.html template.
- Set up URL configurations and static files for the application.

# python-shell-code
'''
from polls.models import user
u = user(first_name = 'abc', last_name = 'cde', email = 'abc@cde.com')
u.save() 

# To see the objects and values 
user.object.all()
user.object.all.values()

# To see specific id
user.objects.get(id=2)
user.objects.filter(id=2).values().first()

# To see id in dic
user.objects.values().get(id=2)

# to update first name for specific id
u = user.objects.get(id=2)
u.first_name = 'rudresh'
u.save()
'''