from data_handler.functions import create_table
from data_handler.functions import data_path, create_list, copy_table
import pandas as pd
from sqlalchemy import create_engine

#df = pd.read_csv('/home/joao_victor/repos/brazilian_election_data_analysis/election_data/perfil_eleitorado_1994.csv', sep = ';' , header = 0, encoding = 'latin1', nrows = 1000, index_col = False, quoting = 1)
#print(df.dtypes)
file_list = create_list(data_path)
create_table(file_list)
copy_table(file_list)

#df = pd.read_csv('/home/joao_victor/repos/brazilian_election_data_analysis/election_data/perfil_eleitorado_2016.csv', sep = ';' , header = 0, encoding = 'latin1', nrows = 1000, index_col = False)
#engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
#df.head(0).to_sql('perfil_eleitorado_2016.csv', engine, if_exists = 'replace', index = False)

