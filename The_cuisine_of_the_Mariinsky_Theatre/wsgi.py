"""
WSGI config for The_cuisine_of_the_Mariinsky_Theatre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'The_cuisine_of_the_Mariinsky_Theatre.settings')

application = get_wsgi_application()
