ARG UBUNTU_VERSION=16.04
FROM ubuntu:$UBUNTU_VERSION

ARG PYTHON_VERSION=2.7.9

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

# Ports
EXPOSE 47
EXPOSE 67


#CMD ["honeyd", "-d", "-f", "honeyd.conf"]
