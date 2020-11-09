import os
from flask_mysqldb import MySQL
from flask import Flask

BASE_DIR = os.getcwd()

TEMPLATE = f"{BASE_DIR}\\frontend\\templates"
STATIC = f"{BASE_DIR}\\frontend\\static"

# Instâncias
__app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)
__db = MySQL(__app)

# DB Config
__app.config.from_object(__name__) # load config from this file
__app.config['MYSQL_HOST'] = '127.0.0.1'
__app.config['MYSQL_USER'] = 'root'
__app.config['MYSQL_PASSWORD'] = ''
__app.config['MYSQL_DB'] = 'jogoteca'
__app.config['MYSQL_port'] = '3306'


# Getters
def getDB():
    return __db


def getApp():
    return __app




