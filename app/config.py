import os
#basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DB_ENDPOINT = os.getenv('DB_ROOT')
    DB_PORT = "3306"
    DB_NAME = "castbuddy"
    DB_USERNAME = "cb_admin"
    DB_PASSWORD = os.getenv('CB_PASS')
