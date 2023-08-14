projeto case 1 - safira

[primeira_etapa]

* docker_fonte

conecta via wget e faz download do arquivo no container
disponibilizar apos descompatar os arquivos num pasta
rodar o docker, o comando mv para o volume configurado: mv /projeto/* /projeto/fontes

* docker_csv

preparar o container para usar driver: DRIVER={Microsoft Access Driver (*.mdb, *.accdb)}
baixar lib
executar o python
- acessar os aqruivos que o docker fonte disponibilizou na estrutura do projeto
- faz uma leitura full dos aqruivos(o arquivo csv foi gerado no storage) e gera um dataframe - pandas
