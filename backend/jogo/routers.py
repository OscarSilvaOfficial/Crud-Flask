from backend.jogo.views import *
from backend.ext.configuration import *

app.add_url_rule('/', 'index', index)
app.add_url_rule('/novo', 'novo', novo)
app.add_url_rule('/create', 'create', create, methods=['POST'])
app.add_url_rule('/editar', 'edit', edit, methods=['POST'])
app.add_url_rule('/editar/<int:id>', 'deletar', deletar)


