import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-backend.configuration.settings')

app = get_wsgi_application()

# os.system("python django-backend/manage.py collectstatic")
# os.system("python django-backend/manage.py runserver")