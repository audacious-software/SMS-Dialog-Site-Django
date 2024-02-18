# Simple SMS Dialog Site

This repository is intended to serve as a starting point for creating interactive SMS-drive text message experiences using Django. It brings together the following technologies from Audacious Software to provide a foundation for more specialized work:

* [Simple Messaging for Django](https://github.com/audacious-software/Simple-Messaging-Django): A self-contained Django app for sending and receiving SMS text messages via services such as Twilio.
* [Django Dialog Engine](https://github.com/audacious-software/Django-Dialog-Engine) (DDE): An abstract state-machine system for conducting structured dialogs between two parties. This component provides the base foundation for running real-time dialogs.
* [Django Dialog Engine Builder](https://github.com/audacious-software/Django-Dialog-Engine-Builder): An editing interface for creating and modifying dialogs used by Django Dialog Engine. This provides a user interface for constructing entire dialogs using the structures provided by DDE to generate the JSON-based dialog definitions used by that framework.
*	[Simple Messaging Dialog Support](https://github.com/audacious-software/Simple-Messaging-Dialog-Engine-Support): A bridge app that allows Django Dialog Engine to be used with Simple Messaging for Django. This app provides the relevant infrastructure that enables interaction between the two components.
*	[Quicksilver](https://github.com/audacious-software/Quicksilver-Django): A task-scheduling app that replaces CRON-based systems to enable second-level task execution for jobs such as sending and receiving real-time responses from the Django Dialog Engine.

In addition to the components above, this site also includes a basic dashboard app that serves as a starting point for building more specific user interfaces to the system.

## Prerequisites

This projects assumes a competent working knowledge of Django and related dependencies. It assumes that a Postgres database has been set-up for use by the site. It also assumes that the site will be configured for public access, to facilitate ongoing management and communication with Twilio and other services providing SMS sending and receipt features.

We highly recommend setting up [a Python 3-based virtual environment](https://docs.python.org/3/library/venv.html) before proceeding.

## Installation

**Step 1:** Clone the site to an appropriate location:

    git clone https://github.com/audacious-software/SMS-Dialog-Site-Django.git /path/to/app/sms_site

**Step 2:** Activate the virtual environment:

    source /path/to/venv/bin/activate

**Step 3:** Install Python dependencies:

    cd  /path/to/app/sms_site
    pip install -r requirements.txt

**Step 4:** Initialize git dependencies:

    git submodule init
    git submodule update

**Step 5:** Configure the local settings:

    cp sms_site/local_settings.py-template sms_site/local_settings.py

Open `sms_site/local_settings.py` in an appropriate editor and configure the locally-specific settings within. Instructions are provided within the file to assist you.

**Step 6:** Create the database, initialize the static files, and create a superuser account:

    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser

**Step 7:** Initialize Quicksilver:

    python manage.py initialize_quicksilver_tasks

This adds the relevant Quicksilver tasks to the system.

Next, add [a CRON job](https://opensource.com/article/17/11/how-use-cron-linux) to start Quicksilver:

    * * * * *    source /path/to/venv/bin/activate &&  python /path/to/app/sms_site/manage.py run_task_queue

This will restart the task execute on restart or interruption. Note that if Quicksilver is killed uncleanly, you can restart it by removing the lock file at

    /tmp/my_site_com__run_task_queue__default.lock

**Step 8**: Initialize Django Dialog Engine builder:

    python manage.py builder_initialize_cards
    python manage.py builder_initialize_template_dialog

**Step 9:** Set up Apache: At this point, you are ready to configure Apache to serve your site. 

Be sure that you've installed a mod_wsgi module that is compatible with Python 3. If you do not have a compatible module, uninstall the existing module and follow the instructions at [the mod_wsgi site](https://pypi.org/project/mod-wsgi/) to compile and install a compatible version.

To connect Apache to Django, create a suitable virtual host and add the following directives:

    WSGIDaemonProcess sms_site python-path=/path/to/venv/lib/python3.8/site-packages:/path/to/app/sms_site/
    WSGIProcessGroup sms_site
    
    WSGIScriptAlias / /path/to/app/sms_site/sms_site/wsgi.py
    Alias /static /path/to/app/sms_site/static
    Alias /media /path/to/app/sms_site/media

Given the sensitive nature of the communications likely to be conveyed by this system, we highly recommend also configuring your virtual host to use an SSL certificate. For a free certificate, visit [Let's Encrypt](https://letsencrypt.org/) for details.

After these steps are complete, you may log into the main site using your superuser credentials:

    https://my-site.example.com/dashboard/

(Replace with proper host name.)

The Django administrative site is available at

    https://my-site.example.com/admin/

From here, you should be able log into the site, create new dialogs, schedule dialogs from the dashboard, and begin development on your particular project.

If you have any questions or encounter any difficulties, e-mail [chris@audacious-software.com](mailto:chris@audacious-software.com) for assistance.






