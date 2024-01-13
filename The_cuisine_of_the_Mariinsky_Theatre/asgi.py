"""
ASGI config for The_cuisine_of_the_Mariinsky_Theatre project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'The_cuisine_of_the_Mariinsky_Theatre.settings')

application = get_asgi_application()
