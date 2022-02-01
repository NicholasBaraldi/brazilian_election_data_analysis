import os
import csv 
import random
import pandas as pd
from pathlib import Path
from zipfile import ZipFile
from sqlalchemy import create_engine
#import psycopg2 as ps    in case you want to upload the full table use this libary

data_path = Path.home()
data_path = data_path.joinpath('repos/brazilian_election_data_analysis/election_data/')

# Function made to extract .csv file downloaded from the crawler
def extractor (file_name):
    for i in file_name:
        with ZipFile(data_path.joinpath(i)) as myZip:
            csv = [file for file in myZip.namelist() if '.csv' in file or '.txt' in file]
            myZip.extractall(members=csv, path=data_path)

# Function made to delete zip files after extraction
def delete (file_name):
    for i in file_name:
        os.remove(data_path.joinpath(i))

# Function made to create a list with the files name
def create_list (data_path):
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(data_path):
        file_list.extend(filenames)
        break
    file_list.sort()
    return file_list

# Function made to create a table with only 10% of the data and upload it to the postgreSQL server
def create_table (file_name):
    num_rows = 0 
    p = 0.1
    for i in file_name:
        with open(f'{data_path}/{i}', 'r', encoding='latin1') as file:
            reader = csv.reader(file)
            lines  = int(len(list(reader)))   
        df = pd.read_csv(data_path.joinpath(i), sep = ';' , header = 0, encoding = 'latin1', skiprows = lambda i: i>0 and random.random() > p, index_col = False, dtype = str)
        engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
        df.to_sql(i, engine, if_exists = 'replace', index = False)
        #df.head(0).to_sql(i, engine, if_exists = 'replace', index = False)  # When using psycopg2 libary use this pice of code to create the table header


#code using psycopg2 libary
'''
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
'''
