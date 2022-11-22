FROM travelping/scapy

RUN apk update \
    add py3-pip

ENTRYPOINT ["sh"]