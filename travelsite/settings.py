"""
Django settings for travelsite project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()

import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")



# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = os.environ.get('DEBUG', 'False') == "False"
print(DEBUG)

ALLOWED_HOSTS = [
     'https://presictravels.onrender.com', 'presictravels.onrender.com', 'localhost', '127.0.0.1', '::1'
    ]

# Application definition

INSTALLED_APPS = [
    'mytravel',
    'account',
    "marketing",
    'myjob',

    'crispy_forms',
    "crispy_bootstrap4",


    # country list display
    'django_countries',

     # for the rich text display
    'ckeditor',
    'ckeditor_uploader',

    # django built in debuging tool
    'debug_toolbar',
     

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# for django debug_toolbar setup

DEBUG_TOOLBAR_CONFIG = {'ENABLE_LOG': True, "ROOT_TAG_EXTRA_ATTRS": "data-turbo-permanent"}
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost",
    # ...
]

# the django debug pannel
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]


MIDDLEWARE = [
    #for the debug tool bar 

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# WHITENOISE_ENABLED = False


ROOT_URLCONF = 'travelsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'travelsite/templates')
        ],
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

WSGI_APPLICATION = 'travelsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'prisictravels-a',
'USER': USER,
'PASSWORD': PASSWORD, # Replace with the actual password
'HOST': 'dpg-cs66b7ij1k6c73a08g5g-a',
'PORT': '5432',
}
}

DATABASE_URL = os.getenv('DATABASE_URL ')
# DATABASES = {
#     'default': dj_database_url.parse(os.getenv('DATABASE_URL'))
#     }

# this will enable database update from development environmet
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# added the staticfiles_storage for compresing and catching of our staticfiles
# this solve the server error problem for me
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

# this will exclude the file path which may causing the server error
# STATICFILES_EXCLUDE = ['travelsite/vendor/bootstrap/css/bootstrap-grid.css.map']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

CKEDITOR_UPLOAD_PATH = 'content/ckeditor/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'travelsite/static'),
  
]


# this will log bug to console even when debug is set to False.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # 'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            #'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
 
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
