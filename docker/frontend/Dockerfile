FROM node:18.17.1

USER root

RUN apt-get update
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

WORKDIR /app

COPY package.json /app
COPY package-lock.json /app

RUN npm install
