FROM ubuntu:24.04

RUN sed -i -e 's/http:\/\/archive\.ubuntu\.com\/ubuntu\//http:\/\/us-west-2\.ec2\.archive\.ubuntu\.com\/ubuntu\//' /etc/apt/sources.list.d/ubuntu.sources
RUN sed -i -e 's/http:\/\/security\.ubuntu\.com\/ubuntu\//http:\/\/us-west-2\.ec2\.archive\.ubuntu\.com\/ubuntu\//' /etc/apt/sources.list.d/ubuntu.sources
# RUN ls /etc/apt/sources.list.d
# RUN cat /etc/apt/sources.list.d/ubuntu.sources

WORKDIR /app

RUN apt-get update
RUN apt-get install -y apt-utils curl git build-essential python3-dev python3.12-venv libldap2-dev libsasl2-dev slapd ldap-utils

RUN python3 -m venv /app/venv
RUN . /app/venv/bin/activate && pip install -U wheel pip

ADD . sms_site

WORKDIR /app/sms_site

RUN . /app/venv/bin/activate && pip install -r /app/sms_site/requirements.txt

ADD ./docker/django/local_settings.py /app/sms_site/sms_site/local_settings.py
ADD ./docker/django/wsgi.py /app/sms_site/sms_site/docker_wsgi.py

ADD ./docker/django/django.sh /app/django.sh

EXPOSE ${DJANGO_WEB_PORT}