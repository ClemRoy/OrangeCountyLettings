# pull the official base image
FROM python:3.9-alpine3.13
LABEL "website.name"="oc_lettings"
# set work directory
WORKDIR /app
ENV PORT 8000
EXPOSE $PORT

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY = $SECRET_KEY
ARG COMMIT_HASH=unspecified
LABEL git_commit=$COMMIT_HASH

# copy project
COPY . /app

# install dependencies
COPY ./requirements.txt /requirements.txt

RUN python -m venv /env && \
    source /env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app && \
    python manage.py collectstatic --noinput

ENV PATH="/env/bin:$PATH"

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT