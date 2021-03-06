from backend.auth.views import *
from backend.ext.configuration import *

app = getApp()

app.add_url_rule('/login', 'login', login)
app.add_url_rule('/logout', 'logout', logout)
app.add_url_rule('/autenticar', 'autenticar', autenticar, methods=['POST'])
app.add_url_rule('/criaUsuario', 'criaUsuario', criaUsuario, methods=['POST'])