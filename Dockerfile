FROM ubuntu:22.04

WORKDIR /app/

RUN apt-get -qq update

RUN apt-get clean && apt-get update && apt-get install -y locales

# Setup the environment
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

# Turn off Interactive mode for the Python Installs
ENV DEBIAN_FRONTEND noninteractive

# Install the supported versions of python
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.7 python3.7-distutils python3.7-dev
RUN apt-get install -y python3.8 python3.8-distutils python3.8-dev
RUN apt-get install -y python3.9 python3.9-distutils python3.9-dev
RUN apt-get install -y python3.10 python3.10-distutils python3.10-dev
RUN apt-get install -y python3.11 python3.11-distutils python3.11-dev

# Install and update PIP
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip

# Transfer the requirements over
COPY requirements.txt .
COPY requirements_dev.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_dev.txt