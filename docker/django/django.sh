#!/bin/bash

echo SMS_SITE: Starting SMS Site server...
source /app/venv/bin/activate

cd /app/sms_site

echo SMS_SITE: Initializing database and static resources...

mkdir -p /app/sms_site/media/simple_data_export_uploads
mkdir -p /app/sms_site/media/incoming_message_media
mkdir -p /app/sms_site/media/outgoing_message_media

echo SMS_SITE: Creating/updating database...

python3 manage.py migrate --skip-checks

echo SMS_SITE: Creating/updating Quicksilver tasks...

python3 manage.py install_quicksilver_tasks --skip-checks

echo SMS_SITE: Clearing ongoing Quicksilver tasks...

python3 manage.py clear_ongoing_executions --before-minutes 0 -v 3 --skip-checks

echo SMS_SITE: Creating/updating dialog cards tasks...

python3 manage.py builder_initialize_cards

echo SMS_SITE: Creating/updating superuser...

python3 manage.py docker_update_data docker/data/users.json -v 3

echo SMS_SITE: Creating/updating generative AI models...

python3 manage.py docker_update_data docker/data/simple_generative_ai.json -v 3

echo SMS_SITE: Creating/updating dialogs...

python3 manage.py docker_update_data docker/data/scripts.json -v 3

echo SMS_SITE: Creating/updating channels...

python3 manage.py docker_update_data docker/data/channels.json -v 3

python3 manage.py collectstatic --no-input

echo SMS_SITE: Validating installation...

python3 manage.py check

echo Installing and starting gunicorn...
pip install gunicorn
gunicorn sms_site.wsgi --log-file - --capture-output --enable-stdio-inheritance --workers 4 --bind="0.0.0.0:$DJANGO_WEB_PORT"

# Uncomment the line below if running on a local machine, and not a server container host.
# echo SMS_SITE: Starting built-in Django web server on port $DJANGO_WEB_PORT...

# python3 manage.py runserver 0.0.0.0:$DJANGO_WEB_PORT
