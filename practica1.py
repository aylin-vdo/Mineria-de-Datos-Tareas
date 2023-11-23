import subprocess
import zipfile

#primero: pip install kaggle
#descargar api key json, y colocar en .kaggle de la carpeta user
api_command = "kaggle datasets download -d liqiang2022/china-techgiant-stock-data-in-hk-market-2022"

subprocess.run(api_command, shell=True)

with zipfile.ZipFile('china-techgiant-stock-data-in-hk-market-2022.zip', 'r') as zip_ref:
    zip_ref.extractall()

import os
os.remove('china-techgiant-stock-data-in-hk-market-2022.zip')
