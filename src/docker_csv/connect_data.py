
import pyodbc
import pandas
import datetime

import sys
import os
path = os.getcwd()    
print(path)
string_conexao_accdb = f'{path}/fonte/BD_balance_valorizado_2306_Data_BASE_BASE_LT_MEDIDAS.accdb'
string_conexao_mdb = f'{path}/fonte/RETIROS_2306.mdb'

# conn_string = ("DRIVER={MDBTools};"+f"DBQ={string_conexao_accdb}")
# conn = pyodbc.connect(conn_string)

def connect(str_conexao):
    print(f'{str_conexao}')
    conn_string = ("DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};;"+f"DBQ={str_conexao}") 

    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()

    return cursor

# def get_script_sql(file):
#     from google.cloud import storage
#     from mygcpcredencial import my_credencial

#     credentials = my_credencial()
#     # Construct a BigQuery client object.
#     storage_client = storage.Client(credentials=credentials, project='devsamelo2')
    
#     bucket = storage_client.bucket('proj-domestico-file')
#     blob = bucket.blob()
#     # Optional: set a generation-match precondition to avoid potential race conditions
#     # and data corruptions. The request to upload is aborted if the object's
#     # generation number does not match your precondition. For a destination
#     # object that does not yet exist, set the if_generation_match precondition to 0.
#     # If the destination object already exists in your bucket, set instead a
#     # generation-match precondition using its generation number.
#     generation_match_precondition = 0

#     blob.upload_from_filename('/projeto/fonte/csv', if_generation_match=generation_match_precondition)


def tab_from_csv(cursor, tabela):
    
    print(f'Gerar dados da tabela: {tabela}')

    cursor.execute(f'select * from {tabela}')

    coluna = []
    for col in cursor.description:
        coluna.append(col[0])

    linha = []
    for row in cursor.fetchall():
        linha.append(row)

    df = pandas.DataFrame([tuple(t) for t in linha[:1000]], columns=[col for col in coluna])
    
    print(f'Total de dados da tabela: {len(df)}')

    dt = datetime.datetime.today()
    dt_csv = datetime.datetime.strftime(dt,"%d%m%Y%H%M%S")
    df.to_csv(f'csv/{tabela}_{dt_csv}.csv', encoding = 'utf-8', index = False)

    print(f'Nome do CSV gerado da tabela: {tabela}_{dt_csv}.csv')

def connect_mdb():

    #string_conexao_mdb = 'C:\\Users\\andre\\Downloads\\03-Bases-de-Datos\\03 Bases de Datos\\01 Balance Físico\\RETIROS_2306\\RETIROS_2306.mdb'

    cursor = connect(string_conexao_mdb)

    list_tab=[]
    for i in cursor.tables(tableType='Table'):
        print(i.table_name)
        list_tab.append(i.table_name)

    for i in list_tab:
        tab_from_csv(cursor, i)

def connect_accbd():

    #vars().string_conexao_accdb() = 'C:\\Users\\andre\\Downloads\\03-Bases-de-Datos\\03 Bases de Datos\\01 Balance Físico\\BD_balance_valorizado_2306_Data_BASE_BASE_LT_MEDIDAS\\BD_balance_valorizado_2306_Data_BASE_BASE_LT_MEDIDAS.accdb'

    cursor = connect(string_conexao_accdb)

    list_tab=[]

    for i in cursor.tables(tableType='Table'):
        list_tab.append(i.table_name)

    for i in list_tab:
        tab_from_csv(cursor, i)


if __name__ == "__main__":
    connect_accbd()            