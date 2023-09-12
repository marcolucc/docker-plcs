FROM ubuntu:18.04

USER root
WORKDIR /root/
RUN apt-get update && \
    apt-get -y install software-properties-common  nano vim cmake libpthread-stubs0-dev git python-pip autoconf bison build-essential pkg-config bison flex autoconf automake libtool make git python2.7 python-pip sqlite3 cmake sudo 
RUN pip install flask flask-login pyserial pymodbus
RUN add-apt-repository ppa:deadsnakes/ppa
# Install dependencies
RUN apt-get update \
  && apt-get install -y python3.7 -y wget gcc make openssl libffi-dev libgdbm-dev libsqlite3-dev libssl-dev zlib1g-dev \
  && apt-get clean

RUN echo "alias python=python3.7" >> ~/.bashrc
RUN export PATH=${PATH}:/usr/bin/python3.7
RUN sudo /bin/bash -c "source ~/.bashrc"

RUN apt install python3-pip -y
RUN python3 -m pip install --upgrade pip

RUN pip install snmpsim==0.4.7 pyasn1==0.4.8

COPY ./data /data


WORKDIR /home/

RUN sudo apt-get install -y git libevent-dev libdumbnet-dev libpcap-dev libpcre3-dev libedit-dev bison flex libtool automake git zlib1g-dev make
RUN git clone https://github.com/marcolucc/Honeyd.git && git clone https://github.com/SCADACS/snap7.git
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
#RUN chmod +x signatures.sh && ./signatures.sh
WORKDIR /home/snap7/build/unix/
RUN make -f x86_64_linux.mk install

WORKDIR /home/snap7/examples/cpp/x86_64-linux/
RUN make 

WORKDIR /home/

RUN git clone https://github.com/thiagoralves/OpenPLC_v3.git
WORKDIR /home/OpenPLC_v3/
RUN ls -al install.sh
RUN sudo chmod +x install.sh
RUN sudo ./install.sh linux

RUN mkdir /home/OpenPLC_v3/scripts

COPY run.sh /home/OpenPLC_v3/
RUN sudo chmod +x run.sh 
COPY PLC3.st /home/OpenPLC_v3/scripts
COPY launch.sh /home/OpenPLC_v3/launch.sh
COPY libsnap7.so-1200 /usr/lib/libsnap7.so
COPY helper.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/helper.sh

#RUN chmod +x /home/snap7/examples/cpp/x86_64-linux/server && ln -s /home/snap7/examples/cpp/x86_64-linux/server /usr/local/bin/

EXPOSE 502
EXPOSE 6668/udp
EXPOSE 8080
# Ports
EXPOSE 47
EXPOSE 67
EXPOSE 68
EXPOSE 102
EXPOSE 161
#ENTRYPOINT ["snmpsimd.py", "--data-dir=/data", "--agent-udpv4-endpoint=0.0.0.0:1024", "--v2c-arc"]


CMD sudo echo '192.168.10.106  plc1.rete' >> /etc/hosts \
    && echo '192.168.10.107  plc2.rete' >> /etc/hosts \
    && echo '192.168.10.108  plc3.rete' >> /etc/hosts \
    && nohup honeyd -d -f /app/honeyd.conf &> honeyd.log \
    && sh /home/OpenPLC_v3/run.sh \
    && snmpsimd.py --data-dir=/data --agent-udpv4-endpoint=0.0.0.0:161 --v2c-arc


#CMD  server  &; sudo echo '192.168.10.106  plc1.rete' >> /etc/hosts && echo '192.168.10.107  plc2.rete' >> /etc/hosts && echo '192.168.10.108  plc3.rete' >> /etc/hosts; nohup honeyd -d -f /app/honeyd.conf &> honeyd.log; sh /home/OpenPLC_v3/run.sh  

#CMD server

#CMD bash /usr/share/honeyd/s7commServer
#CMD  sudo echo '192.168.10.106  plc1.rete' >> /etc/hosts && echo '192.168.10.107  plc2.rete' >> /etc/hosts && echo '192.168.10.108  plc3.rete' >> /etc/hosts; nohup honeyd -d -f /app/honeyd.conf &> honeyd.log; sh /home/OpenPLC_v3/run.sh && server 
#CMD sh /home/OpenPLC_v3/launch.sh
#WORKDIR /app
#CMD ["honeyd", "-d", "-f", "honeyd.conf"]
#CMD sudo echo '192.168.10.106  plc1.rete' >> /etc/hosts \
#    && echo '192.168.10.107  plc2.rete' >> /etc/hosts \
 #   && echo '192.168.10.108  plc3.rete' >> /etc/hosts \
  #  && nohup honeyd -d -f /app/honeyd.conf &> honeyd.log \
   # && sh /usr/local/bin/helper.sh \
    #&& sh /home/OpenPLC_v3/run.sh 