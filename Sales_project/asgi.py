"""
ASGI config for Sales_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

import django
from django.core.asgi import get_asgi_application
# django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sales_project.settings')

application = get_asgi_application()

# import os
# import django
# from channels.routing import get_default_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Sales_project.settings')
#
# django.setup()
#
# application = get_default_application()