# Use an official Python runtime as a parent image
FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common vim

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN apt-get install -y git

RUN mkdir JobchainSite
COPY requirements.txt /JobchainSite/requirements.txt
RUN pip3 install -r /JobchainSite/requirements.txt --user
RUN mkdir JobchainSite/src
COPY src/* /JobchainSite/src/
WORKDIR "JobchainSite/src"
EXPOSE 8080
CMD python3 server.py
