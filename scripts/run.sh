#!/bin/sh

set -o errexit

/usr/local/bin/dockerize -timeout 60s -wait tcp://${POSTGRES_HOST}:${POSTGRES_PORT}
python manage.py migrate
sh /app/scripts/run_tests.sh