FROM python:3.10.6
ENV PYTHONUNBUFFERD=1
WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt
