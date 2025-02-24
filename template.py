import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name="cnnClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "demo.py"   
]


for path in list_of_files:
    path=Path(path)
    file_dir,filename=os.path.split(path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
    if (not os.path.exists(path)) or (os.path.getsize(path)==0):
        with open(path,"w") as f:
            pass
            logging.info(f"Creating empty file: {path}")
    
    else:
        logging.info(f"{filename} already exists")

