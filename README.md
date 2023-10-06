# prepare

```
pyenv shell 3.11.5
python -m venv venv
source venv/bin/activate
pip install django
django-admin startproject conf .
```

# remove

* `DEBUG`
* `ALLOWED_HOSTS`
* `INSTALLED_APPS`
* `MIDDLEWARE`
* `ROOT_URLCONF`
* `TEMPLATES` 
* `WSGI_APPLICATION`
* `AUTH_PASSWORD_VALIDATORS`
* `LANGUAGE_CODE`
* `TIME_ZONE`
* `USE_I18N`
* `USE_TZ`
* `STATIC_URL`

# fixtures

```
python manage.py dumpdata myapp.Role --output fixtures/role.json
```

# reset migrations

```
python manage.py migrate --fake myapp zero
python manage.py makemigrations
python manage.py migrate --fake-initial
```