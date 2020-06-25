FROM python:3.8-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app/

RUN gunicorn wsgi:app

EXPOSE 8080

CMD ["gunicorn", "wsgi:app"]