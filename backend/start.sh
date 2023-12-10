#!/bin/bash

# migrations 
python manage.py makemigrations
python manage.py migrate
# locales
python manage.py compilemessages
# run command
python manage.py runserver