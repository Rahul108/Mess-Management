"""
Django settings for Mess-Management.
"""

import environ
from pathlib import Path

import pgconnection
import structlog
import os



# Load environment Varialbe
BASE_DIR = environ.Path(__file__) - 2


# Load environment variables
env = environ.Env()
DJANGO_ENV = env.str("DJANGO_ENV", default="development")

env_file = BASE_DIR(".env")
env.read_env(env_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}

DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "#/password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "LOGOUT_ON_PASSWORD_CHANGE": True,
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'
CORS_ORIGIN_ALLOW_ALL = True

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
            ],
        },
    },
]

WSGI_APPLICATION = 'api.wsgi.application'


# Database
DATABASES = pgconnection.configure({
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DATABASE_NAME", default="messmanagement"),
        "USER": env.str("DATABASE_OWNER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST", default="localhost"),
        "PORT": env.int("DATABASE_PORT", default=5432),
    },
})



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = env.str("DEFAULT_TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = BASE_DIR("static")
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    BASE_DIR("assets"),
]

# User uploaded media files
MEDIA_ROOT = env.str("MEDIA_ROOT")
MEDIA_URL = "/media/"

# Site specific settings
SITE_NAME = env.str("SITE_NAME")
ADMIN_SITE_HEADER = env.str("ADMIN_SITE_HEADER")
API_BROWSER_HEADER = env.str("API_BROWSER_HEADER")

SETTINGS_EXPORT = [
    "SITE_NAME",
    "ADMIN_SITE_HEADER",
    "API_BROWSER_HEADER",
]

CACHES = {
    'default': {
        'BACKEND': 'djpymemcache.backend.PyMemcacheCache',
        'LOCATION': [
            '127.0.0.1:11211',
        ]
    }
}


