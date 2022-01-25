"""
Django settings for dextre project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# Application definition
INSTALLED_APPS = [
    "lib",
    "blog",
    "accounts",
    "events",
    "api",
    "report",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.table_block",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.core",
    "modelcluster",
    "taggit",
    "taggit_templatetags2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "oauth2_provider",
    "corsheaders",
    "djangobower",
    "compressor",
    "anymail",
    "markdownx",
    "widget_tweaks",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    #    'wagtail.core.middleware.SiteMiddleware',
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "dextre.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dextre.wsgi.application"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = "en-gb"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "djangobower.finders.BowerFinder",
    "compressor.finders.CompressorFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Django Compressor
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, "../components"))
COMPRESS_PRECOMPILERS = (
    (
        "text/x-scss",
        "sass --style compressed"
        ' -I "%s/bower_components/foundation-sites/scss"'
        ' -I "%s/bower_components/bulma"'
        ' -I "%s/bower_components/motion-ui"'
        ' {infile} "{outfile}"'
        % (BOWER_COMPONENTS_ROOT, BOWER_COMPONENTS_ROOT, BOWER_COMPONENTS_ROOT),
    ),
)

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
    "django.contrib.auth.hashers.SHA1PasswordHasher",
    "django.contrib.auth.hashers.MD5PasswordHasher",
    "django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher",
    "django.contrib.auth.hashers.UnsaltedMD5PasswordHasher",
    "django.contrib.auth.hashers.CryptPasswordHasher",
]

# Anymail
DEFAULT_FROM_EMAIL = "noreply@uwcs.co.uk"

# Django-bower
BOWER_INSTALLED_APPS = ["bulma~0.9.0"]

# OAuth2 groups
OAUTH2_PROVIDER = {
    "SCOPES": {
        "read": "Read scope",
        "write": "Write scope",
        "seating": "Pick, move, and unpick seats for a UWCS LAN event",
        "event": "Access to sign up to and deregister from UWCS events",
        "lan": "Access to your nickname and seat location at UWCS LANs",
        "lanapp": "Access to your name, nickname, and university ID for LAN applications",
        "roles": "Access to your nickname and whether or not you are or have been a member of the exec committee",
        "profile": "Access to your name, nickname, university ID",
    },
    "DEFAULT_SCOPES": {"event"},
}

REQUEST_APPROVAL_PROMPT = "auto"

ACCESS_TOKEN_EXPIRE_SECONDS = 86400

# WarwickSU Membership API key
UNION_API_KEY = "insert-api-key"

# Wagtail settings
WAGTAIL_SITE_NAME = "UWCS (Dextre)"
WAGTAIL_FRONTEND_LOGIN_URL = "/accounts/login/"

# Cross-origin Requests
CORS_ORIGIN_ALLOW_ALL = True

# X-frame Requests
X_FRAME_OPTIONS = "SAMEORIGIN"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "uwcs.co.uk"

# Apache template conf
APACHE_SSL_CIPHER_SUITE = ""
APACHE_SSL_CERT_FILE = ""
APACHE_SSL_KEY_FILE = ""
APACHE_SSL_CHAIN_FILE = ""
APACHE_SITES_AVAILABLE = ""
APACHE_SITES_ENABLED = ""
APACHE_WEBSITE_DIR = ""

# Celery
BROKER_URL = "redis://localhost:6379"
CELERY_RESULT_BACKEND = "redis://localhost:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "GMT"
