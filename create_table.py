from zip_handler.functions import create_table
from zip_handler.functions import data_path, create_list

file_list = create_list(data_path)
create_table(file_list)