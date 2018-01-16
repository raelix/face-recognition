#!/bin/bash


# Check and install dlib

pip list dlib &> /dev/null
if [ "$?" != 0 ]; then
cd ~ && \
    mkdir -p dlib && \
    git clone https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python setup.py install --yes USE_AVX_INSTRUCTIONS
fi


# Setting SSH server

echo "root:hammer" | chpasswd
cp sshd_config /etc/ssh/
service ssh restart


# Postgres init

echo "Trying to wait postgres"
until psql -h "db" -p 5432 -U "postgres" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres is up..."


# Avoid exit 

while true; do sleep 1; done
