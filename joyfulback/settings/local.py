from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "joyful-village",
        "USER": "joyful",
        "PASSWORD": "joyful",
        "HOST": "localhost",
        "PORT": "5432",
    }
}



DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# INSTALLED_APPS += ["debug_toolbar"]  # Extra apps for local debugging

# MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")