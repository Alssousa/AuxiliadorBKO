import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('CH4VE_S3GUR4', "CH4V3 P4DR40")
    debug = False