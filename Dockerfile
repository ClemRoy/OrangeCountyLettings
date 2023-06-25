# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /app
EXPOSE 8000

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY=SECRET_KEY

# copy project
COPY . /app

# install dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python manage.py collectstatic

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]