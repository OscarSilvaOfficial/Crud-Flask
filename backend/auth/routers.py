from .views import *
from ext.configuration import *

app.add_url_rule('/login', 'login', login)
app.add_url_rule('/logout', 'logout', logout)
app.add_url_rule('/autenticar', 'autenticar', autenticar, methods=['POST'])