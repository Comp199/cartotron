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

STRIPE_PUBLISH_KEY = 'pk_test_bz5u6SxpNFkuLG7316AZCDIw'
STRIPE_SECRET_KEY = 'sk_test_rYvENk4VhloQpXzsLzOU1JIH'