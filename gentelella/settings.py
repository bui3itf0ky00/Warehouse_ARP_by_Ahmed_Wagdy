"""
Django settings for gentelella project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.conf.global_settings import DATABASES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8*md2t)o**67@*yhc(d=f@j95kl(dnf^rmm4s00$-mh_vurb2b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'imagekit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'gentelella.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'gentelella.context_processors.include_company',
                'gentelella.context_processors.include_farm',
                'gentelella.context_processors.include_job',
                'gentelella.context_processors.include_current_time',
                'gentelella.context_processors.include_farm_no_company',
                'gentelella.context_processors.include_balances',

            ],
        },
    },
]

# Activate Django-Heroku.


WSGI_APPLICATION = 'gentelella.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES['default'] = dj_database_url.config()

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
    os.path.join(BASE_DIR, 'media'),

]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'

try:
    from .local_settings import *
except ImportError:
    pass
