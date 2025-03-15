# Python Script to create the folder Structure of the project

import os
from pathlib import Path
import logging


# Create a Logging Stream

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helpers.y",
    "src/prompt.y",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath) # converts the path to OS specific
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for filename {filename}")
    
    # creating the file
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Created an empty file {filepath}")
        
    else:
        logging.info(f"{filename} already exists")

