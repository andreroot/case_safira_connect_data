# pull official base image
#FROM python:3.9.2-slim-buster

# define a imagem base
FROM debian:latest

#Download appropriate package for the OS version
#Choose only ONE of the following, corresponding to your OS version

# install system dependencies
RUN apt-get update \
  && apt-get -y install wget python3 \
  && apt install python3-venv python3-pip \
  && apt-get clean

RUN wget https://packages.microsoft.com/keys/microsoft.asc
#Debian 11
RUN wget https://packages.microsoft.com/config/debian/11/prod.list

RUN apt-get update \
  && apt-get -y install g++ \
  && apt-get -y install unixodbc unixodbc-dev libpq-dev libstdc++6 libgssapi-krb5-2 
  
RUN apt-get install -y msodbcsql18
RUN apt-get install -y mssql-tools18

ENV PATH="$PATH:/opt/mssql-tools18/bin"

# define o mantenedor da imagem
LABEL maintainer="case1"

#gerar pasta para descompatar
RUN mkdir projetos

WORKDIR /projetos

COPY requirements.txt /projetos

#gerar pasta para descompatar
RUN mkdir fonte

#copia arquivo para pasta das fontes do container
COPY fonte/* /projetos/fonte

RUN mkdir fonte/csv

# RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY connect_data.py /projetos
ENV PYTHONPATH="/pip:/projetos"

# Volumes (Host/Container)
VOLUME /home/andrejagan_gmail_com/projeto/safira_case_1/docker_python/fonte /projeto/fontes/

#ENTRYPOINT ["python"]

CMD ["python","/projetos/connect_data.py"] 