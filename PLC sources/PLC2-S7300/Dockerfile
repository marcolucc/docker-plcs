FROM ubuntu:18.04

USER root
WORKDIR /root/
RUN apt-get update && \
    apt-get -y install git python-pip autoconf bison build-essential pkg-config bison flex autoconf automake libtool make git python2.7 python-pip sqlite3 cmake sudo
RUN pip install flask flask-login pyserial pymodbus

# Install dependencies
RUN apt-get update \
  && apt-get install -y wget gcc make openssl libffi-dev libgdbm-dev libsqlite3-dev libssl-dev zlib1g-dev \
  && apt-get clean


WORKDIR /home/

RUN apt-get update 
RUN apt-get install -y git libevent-dev libdumbnet-dev libpcap-dev libpcre3-dev libedit-dev bison flex libtool automake git zlib1g-dev make
RUN git clone https://github.com/marcolucc/Honeyd.git
WORKDIR Honeyd

RUN mv configure.in configure.ac
RUN ./autogen.sh
RUN ./configure

RUN make 
RUN make install 

# Copy the script to the image
COPY signatures.sh /app/signatures.sh
WORKDIR /app
ADD honeyd.conf /app/honeyd.conf

# Set the script as the command to run when the container starts
RUN ./signatures.sh

WORKDIR /home/

RUN git clone https://github.com/thiagoralves/OpenPLC_v3.git
WORKDIR /home/OpenPLC_v3/
RUN ls -al install.sh
RUN sudo chmod +x install.sh
RUN sudo ./install.sh linux

RUN mkdir /home/OpenPLC_v3/scripts

COPY run.sh /home/OpenPLC_v3/
RUN sudo chmod +x run.sh
COPY PLC2.st /home/OpenPLC_v3/scripts
COPY launch.sh /home/OpenPLC_v3/launch.sh

EXPOSE 502
EXPOSE 6668/udp
EXPOSE 8080
# Ports
EXPOSE 47
EXPOSE 67
EXPOSE 68

CMD nohup honeyd -d -f /app/honeyd.conf &> honeyd.log; sh /home/OpenPLC_v3/run.sh
#CMD sh /home/OpenPLC_v3/launch.sh
#WORKDIR /app
#CMD ["honeyd", "-d", "-f", "honeyd.conf"]