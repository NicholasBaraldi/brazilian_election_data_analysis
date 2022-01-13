from zipfile import ZipFile

def extractor (file_name):
    for i in file_name:
        with ZipFile('/home/nicholas/Repos/brazilian_election_data_analysis/election_data/' + i) as myZip:
            csv = [file for file in myZip.namelist() if '.csv' in file or '.txt' in file]
            myZip.extractall(members=csv, path='/home/nicholas/Repos/brazilian_election_data_analysis/election_data')
