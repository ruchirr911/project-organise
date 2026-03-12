import os
import shutil
from main import sorter
from input import input_folder_path, user_prompt
import logging
base_path = input_folder_path
categories = sorter(input_folder_path, user_prompt)
# creating subfolders

logging.basicConfig(
                    filename="logs/log.txt",
                    level=logging.INFO,
                   format="%(asctime)s - %(levelname)s - %(message)s"
            )
for category, file_list in categories.items():
    #creating path
    folder_path = os.path.join(base_path, category)
    # os command to create folder
    os.makedirs(folder_path, exist_ok=True)
    # iterating through the file list to 
    for file in file_list:
        src = os.path.join(base_path, file)
        dst = os.path.join(folder_path, file)

        if os.path.exists(src):
            if file.startswith("."):
                continue
            else:
                try:
                    shutil.move(src, dst)
                except:    
                    logging.error("file not found")
        else:
            logging.error(f"File not found: {src}")
            print(f"File not found: {src}")
            