import os
from pathlib import Path
from zipfile import ZipFile
import pandas as pd
from sqlalchemy import create_engine
import psycopg2 as ps 

data_path = Path.home()
data_path = data_path.joinpath('repos/brazilian_election_data_analysis/election_data/')

def extractor (file_name):
    for i in file_name:
        with ZipFile(data_path.joinpath(i)) as myZip:
            csv = [file for file in myZip.namelist() if '.csv' in file or '.txt' in file]
            myZip.extractall(members=csv, path=data_path)

def delete (file_name):
    for i in file_name:
        os.remove(data_path.joinpath(i))

def create_list (data_path):
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(data_path):
        file_list.extend(filenames)
        break
    file_list.sort()
    return file_list

def create_table (file_name):
    for i in file_name:
        df = pd.read_csv(data_path.joinpath(i), sep = ';' , header = 0, encoding = 'latin1', nrows = 1000, index_col = False, dtype= str)
        engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
        df.head(0).to_sql(i, engine, if_exists = 'replace', index = False)

def copy_table (file_list):
    engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
    conn = engine.raw_connection() 
    cur = conn.cursor()
    for i in file_list:
        #print(f"\\copy \"{i}\" from '{data_path}/{i}' DELIMITER ';' ENCODING 'latin1' csv header")
        with open(f'{data_path}/{i}', 'r', encoding='latin1') as file:
            file.readline
            cur.copy_from(file, i, sep = ';')
            conn.commit()
    cur.close()
    conn.close()
    