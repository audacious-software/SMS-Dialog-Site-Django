from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'CHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEMECHANGEME' # nosec
DEBUG = False

ALLOWED_HOSTS = ['example.com']

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

SIMPLE_MESSAGING_TWILIO_CLIENT_ID = 'CHANGEME' # nosec
SIMPLE_MESSAGING_TWILIO_AUTH_TOKEN = 'CHANGEME' # nosec
SIMPLE_MESSAGING_TWILIO_PHONE_NUMBER = 'CHANGEME' # nosec

SIMPLE_MESSAGING_COUNTRY_CODE = 'US'

SILENCED_SYSTEM_CHECKS = [
    'security.W004'
    'simple_messaging.W002',
    'simple_messaging_switchboard.E001',
    'simple_messaging_switchboard.E002',
]
