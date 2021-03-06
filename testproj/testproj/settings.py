"""
Django settings for testproj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import psycopg2
import urlparse
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

IS_LOCALHOST = not "DATABASE_URL" in os.environ

#default to empty
TEMPLATE_DIRS = (
    'C:/Python27/django/CS169/testproj/mytemplates/', #always use forward slash
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l=e1%mmj7*o^kit!e97k93x&ot_gp$_#vf^0^*9a5f=fzv+x=w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'loginCount',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'testproj.urls'

WSGI_APPLICATION = 'testproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
#import dj_database_url 
#DATABASES['default'] = dj_database_url.config()

if IS_LOCALHOST:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'loginCounter.db',
        }
    }
else:
    import dj_database_url
    DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

import sys
if 'test' in sys.argv:
    print "======================YOU ARE IN A TEST======================"
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'PST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#import dj_database_url
#DATABASES['default'] = dj_database_url.config()
