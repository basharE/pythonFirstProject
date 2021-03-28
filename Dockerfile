FROM python:3.8-slim-buster
ADD . /app
WORKDIR /app
RUN pip3 install flask requests selenium psycopg2-binary
EXPOSE 5000
VOLUME /app/logs
CMD python3 rest_app.py