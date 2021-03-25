FROM python:3.7-alpine
ADD . /app
WORKDIR /app
RUN pip3 install flask requests selenium pymysql
EXPOSE 5000
VOLUME /app/logs
CMD python3 rest_app.py