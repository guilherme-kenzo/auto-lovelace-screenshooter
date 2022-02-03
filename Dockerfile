FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get dist-upgrade

RUN pip -m venv venv

RUN source venv/bin/activate

RUN pip install -r requirements.txt

RUN python -m screenshooter
