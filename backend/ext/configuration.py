from flask_mysqldb import MySQL
from backend.dao import *
from flask import *
import sqlite3
from flask import g

app = Flask(__name__, template_folder="../../frontend/templates", static_folder='../../frontend/static')
db = MySQL(app)
jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

DATABASE = 'C:\\Users\\oscar\\OneDrive\\Área de Trabalho\\Dev\\Crud-Flask\\flaskr.sqlite'