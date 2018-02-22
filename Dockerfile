FROM ubuntu:14.04

RUN apt-get update \
    && apt-get upgrade -y \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python2.7 \
    python2.7-dev \
    build-essential \
    cmake \
    git \
    wget \
    curl \
    libgtk2.0-dev \
    libjpeg-dev \
    pkg-config \
    python-dev \
    python-numpy \
    python-protobuf\
    software-properties-common \
    zip \
    psmisc \
    vim \
    postgresql-client \
    python-psycopg2 \
    sshpass \
    python-skimage \
    openssh-server \
    && apt-get autoremove \
    && apt-get clean

RUN apt-get install -f -y postgresql-client

RUN cd ~ && \
    mkdir -p dlib && \
    git clone https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python setup.py install --yes USE_AVX_INSTRUCTIONS

#RUN pip install face_recognition

