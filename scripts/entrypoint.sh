#!/bin/sh

set -o errexit

if [[ "$1" == "/usr/local/bin/gunicorn" || "$1" == "python" ]]; then
  /usr/local/bin/dockerize -timeout 60s -wait tcp://${POSTGRES_HOST}:${POSTGRES_PORT}
  python /app/manage.py migrate
  python /app/manage.py collectstatic --noinput


fi


exec "$@"
