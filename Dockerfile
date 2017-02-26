FROM ubuntu:latest
FROM python:3.6
FROM node:latest
FROM pitervergara/geodjango
FROM node:latest
# FROM kkarczmarczyk/node-yarn:latest

RUN apt-get update -y 
RUN apt-get install --auto-remove -y python3-pip libgdal-dev

WORKDIR .
ADD requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -Ur requirements.txt

RUN mkdir /vest
ADD ./vest /vest
WORKDIR /vest

#RUN npm install webpack -g
#RUN npm install
#RUN npm run build

#RUN yarn global webpack
#RUN yarn install
#RUN yarn run build
