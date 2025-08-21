FROM ubuntu:24.04

RUN sed -i -e 's/http:\/\/archive\.ubuntu\.com\/ubuntu\//http:\/\/us-west-2\.ec2\.archive\.ubuntu\.com\/ubuntu\//' /etc/apt/sources.list.d/ubuntu.sources
RUN sed -i -e 's/http:\/\/security\.ubuntu\.com\/ubuntu\//http:\/\/us-west-2\.ec2\.archive\.ubuntu\.com\/ubuntu\//' /etc/apt/sources.list.d/ubuntu.sources
# RUN ls /etc/apt/sources.list.d
# RUN cat /etc/apt/sources.list.d/ubuntu.sources

# Add crontab file in the cron directory
ADD ./docker/cron/crontab /etc/cron.d/django

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/django

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Install Ubuntu packages

RUN apt-get update
RUN apt-get install -y apt-utils curl git build-essential python3-dev python3-venv libldap2-dev libsasl2-dev slapd ldap-utils cron gdal-bin ssmtp mailutils moreutils dos2unix

WORKDIR /app

RUN python3 -m venv /app/venv
RUN . /app/venv/bin/activate && pip install -U wheel pip

ADD . sms_site

WORKDIR /app/sms_site

RUN . /app/venv/bin/activate && pip install -r /app/sms_site/requirements.txt

ADD ./docker/django/local_settings.py /app/sms_site/sms_site/local_settings.py
ADD ./docker/django/wsgi.py /app/sms_site/sms_site/docker_wsgi.py

RUN mv /etc/environment /etc/environment.old
ADD ./docker/.env /etc/environment
RUN cat /etc/environment.old >> /etc/environment

RUN dos2unix /etc/environment
RUN find /app -type f -print0 | xargs -0 dos2unix

ADD ./docker/cron/run.sh /app/run.sh
