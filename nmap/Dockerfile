FROM ubuntu:latest

RUN apt-get update && apt-get install -y nmap && apk add nmap-scripts

CMD ["nmap", "--help", ";", "tail", "-f", "/dev/null"]
