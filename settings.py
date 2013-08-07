"""Settings for chadhancock app."""

import os
import local_settings

LANGUAGE_CODE = 'en-us'

# Note: Be sure to provide all of these values in your own local_settings file.
SECRET_KEY = local_settings.SECRET_KEY

DEBUG = local_settings.DEBUG
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS = (
    'django.contrib.contenttypes',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.csrf',
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'urls'
