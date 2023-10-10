import subprocess
import zipfile

#primero: pip install kaggle
#descargar api key json, y colocar en .kaggle de la carpeta user
api_command = "kaggle datasets download -d mexwell/us-software-engineer-jobs"

subprocess.run(api_command, shell=True)

with zipfile.ZipFile('us-software-engineer-jobs.zip', 'r') as zip_ref:
    zip_ref.extractall()

import os
os.remove('us-software-engineer-jobs.zip')
