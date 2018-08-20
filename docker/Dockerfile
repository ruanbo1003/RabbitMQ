FROM python:3.6-alpine

#RUN useradd zabbix

#USER postgresql_user
WORKDIR /app/src

ADD requirements/. /app/requirements

RUN apk update
RUN apk add net-tools
#RUN apk add build-base

ADD docker /app/docker
ADD src /app/src
