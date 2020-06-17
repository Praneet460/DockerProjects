FROM python:3.7.2-alpine

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

RUN apk add python3-dev build-base linux-headers pcre-dev

RUN pip install uwsgi

ADD . /app

CMD ["uwsgi","--ini","wsgi.ini"]

