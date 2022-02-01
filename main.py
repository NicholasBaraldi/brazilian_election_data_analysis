from data_handler.functions import create_table
from data_handler.functions import data_path, create_list

# Calling functions and creating tables

file_list = create_list(data_path)
create_table(file_list)
