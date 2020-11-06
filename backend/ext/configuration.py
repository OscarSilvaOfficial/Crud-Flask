from flask_mysqldb import MySQL
from dao import *
from flask import *

app = Flask(__name__, template_folder="../../frontend/templates", static_folder='../../frontend/static')
db = MySQL(app)
jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)
