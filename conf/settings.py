import json
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read secret json format file
secret_file = BASE_DIR / 'conf' / 'secret.json'

with open(secret_file) as f:
    secrets = json.loads(f.read())

SECRET_KEY = secrets['secretKey']
DEBUG = secrets['debug']
ALLOWED_HOSTS = secrets['allowedHosts']

DATABASES = {
    'default': secrets['database']['default'],
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INSTALLED_APPS = [
    'myapp',
]
