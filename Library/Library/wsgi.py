import os

from django.core.wsgi import get_wsgi_application

settings_module = 'Library.Library.deployment_settings' if os.environ.get('RENDER') else 'Library.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
application = get_wsgi_application()
