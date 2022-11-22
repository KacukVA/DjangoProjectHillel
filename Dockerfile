FROM python:3.10.6
ENV PYTHONUNBUFFERD=1
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
#FROM python:3.8.5-alpine
#ENV PYTHONUNBUFFERED = 1
#
#WORKDIR /app
#COPY . .
#
#RUN apk add --no-cache mariadb-connector-c-dev
#RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
#
#RUN apk add netcat-openbsd
#
#RUN pip install -r requirements.txt
