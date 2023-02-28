FROM python:2.7

RUN pip install shodan

RUN apt update -y && apt upgrade -y && \
    apt install -y nmap && \
    apt install -y git && \
    git clone https://github.com/meeas/plcscan.git 

CMD ["sh", "-c", "shodan && sleep infinity"]