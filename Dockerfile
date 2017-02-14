FROM ubuntu:16.10
FROM python:3.6
FROM pitervergara/geodjango

RUN apt-get update -y && \
    apt-get install --auto-remove -y \
    python3-pip

WORKDIR .
ADD requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -Ur requirements.txt

RUN mkdir /vest;  
WORKDIR /vest


