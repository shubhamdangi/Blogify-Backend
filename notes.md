- Create New folder

@ setting up the virtual env
- python3 -m venv envName
or
- virtualenv envName
- acitvate the env by 'source envName/bin/activate'

@ creating Django app
- pip3 install django
- django-admin startproject projectName
- python3 manage.py startapp appName
- add the app name to the Settings.py
- pip3 install djangorestframework

- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py createsuperuser
@ model/table syntax
- class ModelName(models.Model):
     fieldName = type

     def __str__(self):
        return self.primaryField

