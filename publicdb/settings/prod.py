from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb',
        'USER': 'FAKE USER',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',        
}        
    }

ALLOWED_HOSTS += ['.dam.io.']
