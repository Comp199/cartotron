from cartotron.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cartotron',
        'USER': 'cartotron',
        'PASSWORD': 'cartotron',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
