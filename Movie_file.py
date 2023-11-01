import os
import shutil

from_dir = "C:/Users/sahis_i/Downloads"
to_dir = "C:/Users/sahis_i/Desktop/D_files"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)