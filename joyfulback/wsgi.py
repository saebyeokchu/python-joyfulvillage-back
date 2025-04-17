# """
# WSGI config for joyfulback project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'joyfulback.settings')

# application = get_wsgi_application()

import os
from django.core.wsgi import get_wsgi_application

env = os.getenv("DJANGO_ENV", "docker")  # Default to production
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"joyfulback.settings.{env}")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "joyfulback.settings.docker")

application = get_wsgi_application()