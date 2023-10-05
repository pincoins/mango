# prepare

```
pyenv shell 3.11.5
python -m venv venv
source venv/bin/activate
pip install django
django-admin startproject conf .
```

# remove django.contrib apps

# fixtures

```
python manage.py dumpdata myapp.Role --output fixtures/role.json
```