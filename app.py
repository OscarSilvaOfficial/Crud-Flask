from flask import *
from backend.entities import *

app = Flask(__name__)
app.secret_key = "asdokifhsAFHJQOIURHWEF'12983791283RQIGFE" 

lista = []

@app.route('/')
def index():
    if 'usuario_logado' not in session:
        return redirect('/login')
    else:
        return render_template('components/index.html', titulo='Jogos', lista=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    else:
        return render_template('components/create.html', titulo='Novo Jogo')

@app.route('/create', methods=['POST',])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo) 
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('components/auth/login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'oscar' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'{session["usuario_logado"]} Está logado!')
        proxima_pagina =  request.form['proxima']
        if proxima_pagina != 'vazio':
            return redirect('/{}'.format(proxima_pagina))   
        else:
            return redirect('/')

    else:
        flash('Credenciais incorretas! Insira as credenciáis corretas.')
        return redirect('/login')

@app.route('/logout')
def logout():
    if session.get('usuario_logado'):
        session.clear()
        flash('Usuário deslogado!')
        return redirect('/login')
    else:
        return redirect('/login')

app.run(debug=True)

