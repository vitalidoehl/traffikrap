"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
import site
import django.core.handlers.wsgi

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/traffik-rap/.virtualenvs/traffikrap/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/traffik-rap/www/traffikrap/traffikrap')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# Activate your virtual env
activate_env = os.path.expanduser("/home/traffik-rap/.virtualenvs/traffikrap/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))


application = django.core.handlers.wsgi.WSGIHandler()
