from zipfile import ZipFile
import os 
from pathlib import Path
data_path = Path.home()
data_path = str(data_path.joinpath('repos/brazilian_election_data_analysis/election_data/'))


def extractor (file_name):
    for i in file_name:
        with ZipFile(data_path + '/' + i) as myZip:
            csv = [file for file in myZip.namelist() if '.csv' in file or '.txt' in file]
            myZip.extractall(members=csv, path=data_path)

def delete (file_name):
    for x in file_name:
        os.remove(data_path + '/' + x)