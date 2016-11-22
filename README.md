# Preparation of environment for Windows
Implied that you have installed `python, pip`.
### Virtual Environment:
**In the first time you need:**
1. Install virtualenv via pip:
`pip install virtualenv`
2. Create a virtual environment for a project:
`virtualenv venv`

**Further:**
3. To begin using the virtual environment, it needs to be activated:
`cd venv\Scripts`
`activate`
4. Install packages as usual, for example:
`cd ..\..\`
`pip install requirements.txt`

### Django
**In the first time you need:**
1. Create Django project:
`django-admin startproject <project-name>`

**Further:**
2. Run Django server:
`cd <project-name>`
`python manage.py runserver`