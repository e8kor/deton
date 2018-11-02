FROM python:3

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential curl
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]