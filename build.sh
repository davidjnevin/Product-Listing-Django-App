#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python listings/manage.py collectstatic --no-input
python listings/manage.py migrate
