# define a imagem base
FROM debian:latest

# define o mantenedor da imagem
LABEL maintainer="case1"

# Atualiza a imagem com os pacotes
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
curl \
wget \
fastjar \
unzip \
convmv \
p7zip-full

#gerar pasta para descompatar
RUN mkdir projeto

WORKDIR /projeto

RUN mkdir fontes

RUN wget https://www.coordinador.cl/wp-content/uploads/2023/07/03-Bases-de-Datos.zip
RUN 7z e 03-Bases-de-Datos.zip

#RUN convmv -f cp1252 -t utf8 --notest /projetos/'03 Bases de Datos'/*
RUN convmv -r -f cp860 -t utf8 --notest .
#RUN jar xvf /projeto/'03 Bases de Datos'/'01 Balance Físico'/BD_balance_valorizado_2306_Data_BASE_BASE_LT_MEDIDAS.zip
RUN 7z e /projeto/BD_balance_valorizado_2306_Data_BASE_BASE_LT_MEDIDAS.zip 
RUN 7z e /projeto/RETIROS_2306.zip 
RUN 7z e /projeto/'BBDD Contratos fisicos 2306.zip'

RUN rm -rf *.zip
# Volumes (Host/Container)
VOLUME /home/andrejagan_gmail_com/projeto/safira_case_1/docker_python/fonte /projeto/fontes/
# sudo docker build -t safira-fonte .
#sudo docker run -it -d --name safira-fontes-v5 -v /home/andrejagan_gmail_com/projeto/safira_case_1/docker_python/fonte:/projeto/fontes safira-fonte /bin/bash
#sudo docker exec -it safira-fontes-v5 /bin/bash

CMD ["bash"]