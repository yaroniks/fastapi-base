import os
from dotenv import load_dotenv

load_dotenv()

TITLE = os.getenv('TITLE')
VERSION = os.getenv('VERSION')
SQL_URL = os.getenv('SQL_URL')
