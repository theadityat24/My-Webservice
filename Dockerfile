FROM python:3.6-slim-stretch

RUN apt update
RUN apt install -y python3-dev gcc

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY export_learners /export_learners
COPY wsgi.py /wsgi.py
COPY api.py /api.py


EXPOSE 8080

CMD ["gunicorn", "wsgi:app"]