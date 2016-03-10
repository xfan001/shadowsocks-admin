"""
Django settings for shadowsocks-admin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
import conf
is_localhost = False

BASE_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^zb2i$9jn^_2rtoy&a1tpo&92(gz+$$nm(w8ykdm%clq^a22%!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = is_localhost

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ssmanagement',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'root_urls'

WSGI_APPLICATION = 'wsgi.application'


# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': conf.db_name,
        'USER': conf.db_user,
        'PASSWORD': conf.db_passwd,
        'HOST': conf.db_host,
        'PORT': conf.db_user,
        'CHARSET': 'utf8',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci',
        },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'ssmanagement'),
)

#static files
STATIC_URL = '/static/'
if is_localhost:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#email
EMAIL_USE_TLS = conf.email_use_tls
EMAIL_HOST = conf.email_host
EMAIL_PORT = conf.email_port
EMAIL_HOST_USER = conf.email_host_user
EMAIL_HOST_PASSWORD = conf.email_host_password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#ip
IPV4 = conf.ipv4_addr
IPV6 = conf.ipv6_addr
