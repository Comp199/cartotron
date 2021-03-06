"""
Django settings for cartotron project.
Generated by 'django-admin startproject' using Django 1.8.7.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '20f&_22(24av-n1ab$yv%(m_2_l4knwk&5siajnxm)_r^*ahy('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',
    'bootstrap3',
    'sorl.thumbnail',
    'storages',
    'tinymce',
    'shop',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'shop.middleware.CartMiddleware',
)

ROOT_URLCONF = 'cartotron.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.categories',
                'shop.context_processors.cart',
                'shop.context_processors.stripe',
            ],
        },
    },
]

WSGI_APPLICATION = 'cartotron.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'cartotron.sqlite3',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sql',
#         'NAME': 'cartotron',
#         'USER': 'cartotron',
#         'PASSWORD': 'cartotron',
#         'HOST': '127.0.0.1',
#         'PORT': 5432,
#     }
# }

STRIPE_PUBLISH_KEY = 'pk_test_bz5u6SxpNFkuLG7316AZCDIw'
STRIPE_SECRET_KEY = 'sk_test_rYvENk4VhloQpXzsLzOU1JIH'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

TEMPLATED_EMAIL_FILE_EXTENSION = 'html'

TEMPLATED_EMAIL_DJANGO_SUBJECTS = {
    'invoice': 'Thanks for shopping with us!',
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

MAILGUN_ACCESS_KEY = ''

MAILGUN_SERVER_NAME = ''


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'

