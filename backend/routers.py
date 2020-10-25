from flask import *
from backend.entities import *
from flask_cors import CORS

app = Flask(__name__, template_folder="../frontend/templates", static_folder='../frontend/static')
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})

lista = []

usuario = Usuario('admin', 'Oscar da Silva', 'admin')
usuario2 = Usuario('teste', 'Meu Teste', 'teste')

usuarios = {
    usuario.id: usuario,
    usuario2.id: usuario2
}

@app.route('/api')
def home():
    message = {}
    data = {}

    message['message'] = 'Hello World from Flask!'
    data['status'] = 200
    data['data'] = message
    return jsonify(data)

@app.route('/index')
def index():
    if 'usuario_logado' not in session:
        return redirect('/login')
    else:
        user = usuarios[session['usuario_logado']].nome
        return render_template('components/index.html', titulo='Jogos', lista=lista, user=user)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        user = usuarios[session['usuario_logado']].nome
        return render_template('components/create.html', titulo='Novo Jogo', user=user)

@app.route('/create', methods=['POST',])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo) 
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('components/auth/login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
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
