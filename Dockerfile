FROM python:3.7-alpine3.8
ENV PYTHONUNBUFFERED 1
ARG ENV

WORKDIR /app

COPY requirements/ requirements/
RUN apk update \
# install psycopg2 dependencies
    && apk add --no-cache postgresql-libs \
        zlib-dev \
        jpeg-dev \
    && apk add --no-cache --virtual .requirements-build-deps \
        gcc \
        musl-dev \
        postgresql-dev \
        libffi-dev \
        libxml2-dev \
        libxslt-dev \
# install requirements
    && pip install --no-cache-dir -r requirements/${ENV}.txt \
    && rm -r requirements \
    && apk del .requirements-build-deps

ENV DOCKERIZE_VERSION v0.6.1
RUN wget "https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz" \
    && tar -C /usr/local/bin -xzvf "dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz" \
    && rm "dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz"

COPY . .

EXPOSE 5000
ENTRYPOINT [ "/app/scripts/entrypoint.sh" ]
CMD [ "/usr/local/bin/gunicorn", "project.wsgi", "--bind", "0.0.0.0:8000"]
