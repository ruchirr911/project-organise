import os
import shutil
from main import sorter
from input import input_folder_path, user_prompt
import logging

base_path = input_folder_path
categories = sorter(input_folder_path, user_prompt)
for category, file_list in categories.items():
    
    folder_path = os.path.join(base_path, category)
    
    os.makedirs(folder_path, exist_ok=True)

    for file in file_list:
        src = os.path.join(base_path, file)
        dst = os.path.join(folder_path, file)

        if os.path.exists(src):
                shutil.move(src, dst)
                logging.basicConfig(
                    filename="logs/log.txt",
                    level=logging.INFO,
                   format="%(asctime)s - %(levelname)s - %(message)s"
            )
                logging.error("file not found")
        else:
            print(f"File not found: {src}")
            