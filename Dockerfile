FROM ubuntu:16.10
FROM python:3.6
# FROM redis
# FROM mdillon/postgis

# env POSTGRES_DB geodb
# env POSTGRES_USER admin

RUN apt-get update -y && \
    apt-get install --auto-remove -y \
    python3-pip \
    postgresql-server-dev-all    

WORKDIR .
ADD requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -Ur requirements.txt

RUN mkdir /vest;  
WORKDIR /vest

# RUN mkdir /srv/vest
# RUN mkdir /srv/logs
# RUN mkdir /srv/static
# RUN mkdir /srv/media
# WORKDIR /srv/vest/vest
# COPY . /srv/vest
