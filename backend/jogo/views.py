from flask import *
from .models import *
from ext.configuration import *

def index():
    if 'usuario_logado' not in session:
        return redirect('/login')
    else:
        user = usuario_dao.buscar_por_id([session['usuario_logado']]).nome
        lista = jogo_dao.listar()
        return render_template('components/index.html', titulo='Jogos', lista=lista, user=user)

def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    else:
        user = usuario_dao.buscar_por_id([session['usuario_logado']]).nome
        return render_template('components/create.html', titulo='Novo Jogo', user=user)

def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo) 
    return redirect(url_for('index'))

def edit():
    ident = request.form['id']
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console, ident)
    jogo_dao.salvar(jogo) 
    flash('Jogo alterado!')
    return 'Formulário salvo' 

def deletar(id):
    jogo_dao.deletar(id)
    flash('O jogo foi removido!')
    return redirect('/')

