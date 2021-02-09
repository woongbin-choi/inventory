from .base import *

ALLOWED_HOSTS = ['3.34.238.224','woongb.shop']

STATIC_ROOT = BASE_DIR / 'static/'

STATICFILES_DIRS = []

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybo',
        'USER': 'dbmasteruser',
        'PASSWORD': '!1samyang',
        'HOST': 'ls-266a09787bb1193fb57f62b53100c40eab6a75bf.crbe8p6vmk6u.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}