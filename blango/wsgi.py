"""
WSGI config for blango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

# from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blango.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

# We actually need to change the order of the imports as well, since trying
# to import Django Configuration’s get_wsgi_application will fail
# if DJANGO_CONFIGURATION is not yet defined

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
