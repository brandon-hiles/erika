import os
from os.path import join, dirname
from dotenv import load_dotenv

# Grab environment variables
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Setup SQL Variables
server = os.environ.get("SQL_SERVER")
db = os.environ.get("SQL_DATABASE")
username = os.environ.get("SQL_USERNAME")
password = os.environ.get("SQL_PASSWORD")

class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f"mysql+pymysql://{username}:{password}@{server}/{db}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
