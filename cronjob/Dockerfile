FROM python:3.6-jessie

RUN apt update \
 && apt install -y openvpn \
 && rm -rf /var/lib/apt/lists/*

COPY ./name_ovpn.ovpn ./

WORKDIR /app
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app
