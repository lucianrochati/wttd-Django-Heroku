"""
Django settings for eventex project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
import os
from unipath import Path

BASE_DIR = Path(__file__).parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=5hp6c$#t%!@4pu$q&ght)3o1d-c+2xa1+vellkn523qk_vroc'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', 'heroku.com.br']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'eventex.core',
    'eventex.subscriptions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eventex.urls'

WSGI_APPLICATION = 'eventex.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#
#
DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd4qo2q0kl0tokj',
        'HOST': 'ec2-54-204-47-70.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'remuwyfyvlsjvz',
       'PASSWORD': '9CVx_e_6mI25mxEPoaMEsjySRH'
   }
}


#DATABASES = {
#'default': {
#'ENGINE': 'django.db.backends.sqlite3',
#'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#'NAME': BASE_DIR.child('db.sqlite3'),
#}
#}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'