FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt ./

COPY . /app/

# RUN apk add --no-cache --virtual libpq-dev build-base
RUN apk add --no-cache --virtual build-base g++ libpq-dev libc-dev gcc && pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "app:app", "-k=eventlet", "--bind=0.0.0.0:8080", "--access-logfile=-", "--log-level=INFO"]
