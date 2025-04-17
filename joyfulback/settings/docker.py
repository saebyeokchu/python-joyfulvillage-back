from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'joyful-village', #joyful
        'USER': 'postgres', #joyful
        'PASSWORD': '1234', #joyful
        'HOST': 'db',  #localhost
        'PORT': '5432',
    }
}

print("docker setttings")


DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS += ["storages"]  # If using S3 or cloud storage
