"""
WSGI config for artshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
from django.core.wsgi import get_wsgi_application


path = '/home/Elirton/artshop'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'artshop.settings'


application = get_wsgi_application()


