from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'CHANGEME' # nosec
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':     'circle_test',
        'USER':     'root',
        'PASSWORD': '', # nosec
        'HOST': 'localhost',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR) + '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR) + '/media/'

TIME_ZONE = 'America/Chicago'

SIMPLE_MESSAGING_TWILIO_CLIENT_ID = 'CHANGEME'
SIMPLE_MESSAGING_TWILIO_AUTH_TOKEN = 'CHANGEME'
SIMPLE_MESSAGING_TWILIO_PHONE_NUMBER = 'CHANGEME'
