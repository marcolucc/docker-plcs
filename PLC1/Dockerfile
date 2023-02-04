ARG UBUNTU_VERSION=16.04
FROM ubuntu:$UBUNTU_VERSION

ARG PYTHON_VERSION=2.7.9






#CMD ["honeyd", "-d", "-f", "honeyd.conf"]


# OPENPLC stuff
USER root
WORKDIR /root/
RUN apt-get update && \
    apt-get -y install git python-pip autoconf bison build-essential pkg-config bison flex autoconf automake libtool make git python2.7 python-pip sqlite3 cmake sudo
RUN pip install flask flask-login pyserial pymodbus

WORKDIR /home/
RUN git clone https://github.com/thiagoralves/OpenPLC_v3.git
WORKDIR /home/OpenPLC_v3/
RUN sudo ./install.sh linux

RUN mkdir /home/OpenPLC_v3/scripts

#COPY mbconfig.cfg /home/OpenPLC_v3/scripts

COPY run.sh /home/OpenPLC_v3/
#COPY openplc.py /home/OpenPLC_v3
RUN sudo chmod +x run.sh
COPY PLC1.st /home/OpenPLC_v3/scripts

# Install dependencies
RUN apt-get update \
  && apt-get install -y wget gcc make openssl libffi-dev libgdbm-dev libsqlite3-dev libssl-dev zlib1g-dev \
  && apt-get clean

WORKDIR /tmp/

# Build Python from source
RUN wget https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz \
  && tar --extract -f Python-$PYTHON_VERSION.tgz \
  && cd ./Python-$PYTHON_VERSION/ \
  && ./configure --with-ensurepip=install --enable-optimizations --prefix=/usr/local \
  && make && make install \
  && cd ../ \
  && rm -r ./Python-$PYTHON_VERSION*

WORKDIR /app

# Needs autogeneration

ADD pots/ /app

COPY signature.py /app

RUN apt-get update 
RUN apt-get install -y git libevent-dev libdumbnet-dev libpcap-dev libpcre3-dev libedit-dev bison flex libtool automake git zlib1g-dev make
RUN git clone https://github.com/marcolucc/Honeyd.git

WORKDIR Honeyd

COPY signature.py /app/Honeyd

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

EXPOSE 502
EXPOSE 6668/udp
EXPOSE 8080
# Ports
EXPOSE 47
EXPOSE 67

CMD ["/home/OpenPLC_v3/run.sh"]

