import os
import django_heroku
import dj_database_url
from pathlib import Path
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vhdbuz+&xl-05p3$etxgbac59-)ifu&-d784_t+h-slfmrfvf1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'crispy_forms',
    'Account',
    'Agent',
    'Company',
    'Customer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BGI.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
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

WSGI_APPLICATION = 'BGI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ohrmsdb',
        'USER': 'ohrmsdb_user',
        'PASSWORD': 'rYCzLOMytQXtRhQ0rAneqbXUa3XptJR4',
        'HOST': 'dpg-cljnhe98mmjc73da4kj0-a.oregon-postgres.render.com',
        'PORT': '',
    }
}
database_url = os.environ.get("DATABASES_URL")
# Parse the PostgreSQL database URL
url = "postgres://ohrmsdb_user:rYCzLOMytQXtRhQ0rAneqbXUa3XptJR4@dpg-cljnhe98mmjc73da4kj0-a.oregon-postgres.render.com/ohrmsdb"
parsed_db = dj_database_url.parse(database_url)

# Update the 'default' database configuration

DATABASES['default'].update(parsed_db)


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [BASE_DIR / "static"] # new
STATIC_ROOT = BASE_DIR / "staticfiles" # new
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'File')

GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

#SMTP configuration 

EMAIL_BACKED='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='ephadaniel177@gmail.com'
EMAIL_HOST_PASSWORD='yheffqwwlrjwpqkg'
SESSION_EXPIRE_SECONDS = 300
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
