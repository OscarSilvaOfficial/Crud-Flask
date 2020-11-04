from flask import *
from backend.models import *
from .dao import JogoDao, UsuarioDao
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="../frontend/templates", static_folder='../frontend/static')

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_port'] = '3306'

db = MySQL(app)

jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)

# Flask Router
@app.route('/')
def index():
    if 'usuario_logado' not in session:
        return redirect('/login')
    else:
        user = usuario_dao.buscar_por_id([session['usuario_logado']]).nome
        lista = jogo_dao.listar()
        return render_template('components/index.html', titulo='Jogos', lista=lista, user=user)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        user = usuario_dao.buscar_por_id([session['usuario_logado']]).nome
        return render_template('components/create.html', titulo='Novo Jogo', user=user)

@app.route('/create', methods=['POST',])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo) 
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('components/auth/login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(f'{usuario.nome.upper()} Está logado!')
            proxima_pagina =  request.form['proxima']
            if proxima_pagina != 'vazio':
                return redirect(proxima_pagina)   
            else:
                return redirect(url_for('index'))
        else:
            flash('Credenciais incorretas! Insira as credenciáis corretas.')
            return redirect(url_for('login'))
    else:
        flash('Credenciais incorretas! Insira as credenciáis corretas.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if session.get('usuario_logado'):
        session.clear()
        flash('Usuário deslogado!')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
