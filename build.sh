#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt
py manage.py collectstatic --noinput
py manage.py migrate
py manage.py loaddata users
py manage.py loaddata initial_data