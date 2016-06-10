from settings import *
import os

# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'


STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_BUCKET']

STRIPE_PUBLISH_KEY = os.environ['STRIPE_PUBLISH_KEY']
STRIPE_SECRET_KEY = os.environ['STRIPE_SECRET_KEY']

EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']
EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ['MAILGUN_SMTP_LOGIN']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'