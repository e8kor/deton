FROM python:3

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential curl
COPY . /app
WORKDIR /app
ENV FLASK_ENV 'production'
ENV FLASK_APP 'src'
ENV FLASK_RUN_PORT 4140
ENV APP_CONFIG '/app/instance/config/app.cfg'
ENV REDIS_PASSWORD 'changeme'
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]