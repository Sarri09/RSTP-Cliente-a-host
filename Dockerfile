FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y tzdata wget
RUN apt-get install -y libcurl4 openssl gnupg unzip zip curl nano git texlive tcpdump
RUN apt-get install -y python3.11 python3-pip
RUN apt-get install -y iptables net-tools inetutils-ping
RUN apt-get install -y iproute2

RUN pip install --pre scapy[complete]
COPY MitM.py $HOME/
COPY Inyeccion.py $HOME/
COPY Inyeccion2.py $HOME/

ENTRYPOINT ["sh"]
