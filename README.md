# HotFix
HitFix patch manager

# Design
1. Backend: Restful API 
2. Frontend: Web-apps
3. Using external storage services

# Ref
* [Quickstart](http://www.django-rest-framework.org/tutorial/quickstart/) 
* [Django Modle FieldType](https://docs.djangoproject.com/en/1.11/ref/models/fields/)

# Requirements
* Python 3.6+
* Django 1.11.4+


# A-line-Shell
cmdline help
```
# init project
django-admin.py startproject project
django-admin.py startapp app
cd ..

# init database 
python3.6 manage.py migrate
python3.6 manage.py createsuperuser


# reinit database
python3.6 manage.py makemigrations
python3.6 manage.py migrate
python3.6 manage.py showmigrations

# run
python3.6 manage.py runserver 0.0.0.0:8000
```

# TODO
* ratelimit
  https://djangopackages.org/packages/p/django-ratelimit/
* client workflow
  1. checkout update
    param: app\_version,key,sign,
    return: rsa,downloada\_url
  2. download patch
  3. report update status
