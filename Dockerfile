FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt ./

COPY . /app/

RUN apk add --no-cache --virtual build-dependencies libpq-dev build-base

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "app:app", "-k=eventlet", "--bind=0.0.0.0:8080", "--access-logfile=-", "--reload"]
