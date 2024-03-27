import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://developer@localhost/almacen_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
