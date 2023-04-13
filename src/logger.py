import logging 
import os
from datetime import datetime


logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,"logs")
with open(LOG_FILE_PATH,"w") as f:
    f.write("========================Logging started======================== \n\n\n")
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)