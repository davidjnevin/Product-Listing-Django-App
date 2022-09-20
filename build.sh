#!/usr/bin/env bash
# exit on error
set -o errexit

/opt/render/project/src/.venv/bin/python -m pip install --upgrade pip
poetry install

python listings/manage.py collectstatic --no-input
python listings/manage.py migrate
