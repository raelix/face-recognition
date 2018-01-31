# Note from Brandon on 2015-01-13:
#
#   Always push this from an OSX Docker machine.
#
#   If I build this on my Arch Linux desktop it works fine locally,
#   but dlib gives an `Illegal Instruction (core dumped)` error in
#   dlib.get_frontal_face_detector() when running on OSX in a Docker machine.
#   Building in a Docker machine on OSX fixes this issue and the built
#   container successfully deploys on my Arch Linux desktop.
#
# Building and pushing:
#   docker build -f opencv-dlib-torch.Dockerfile -t opencv-dlib-torch .
#   docker tag <tag of last container> bamos/ubuntu-opencv-dlib-torch:ubuntu_14.04-opencv_2.4.11-dlib_18.16-torch_2016.03.19
#   docker push bamos/ubuntu-opencv-dlib-torch:ubuntu_14.04-opencv_2.4.11-dlib_18.16-torch_2016.03.19

FROM ubuntu:14.04

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --fix-missing \
    build-essential \
    ca-certificates \
    gcc \
    git \
    libpq-dev \
    make \
    python-pip \
    python2.7 \
    python2.7-dev \
    ssh \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libboost-all-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
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
    && apt-get autoremove \
    && apt-get clean

RUN apt-get install -f -y postgresql-client
    #apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python setup.py install --yes USE_AVX_INSTRUCTIONS

RUN pip install -U "setuptools==3.4.1"
RUN pip install -U "pip==1.5.4"
RUN pip install -U "Mercurial==2.9.1"
RUN pip install -U "virtualenv==1.11.4"
RUN pip install face_recognition

