FROM ubuntu:latest

COPY . /app

RUN apt-get update && apt-get install -y \
    python2.7 \
    python-pip \
    nano \
    snmp \
    && rm -rf /var/lib/apt/lists/*

CMD tail -f /dev/null

