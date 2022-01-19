import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('/home/joao_victor/repos/brazilian_election_data_analysis/election_data/perfil_eleitorado_1994.csv', sep = ';' , header = 0, encoding = 'latin1')
engine = create_engine('postgresql://postgres:mysecretpassword@localhost:5432/postgres')
df.to_sql('perfil_eleitorado_1994', engine)