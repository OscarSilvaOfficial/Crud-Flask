from flask import render_template, url_for, redirect, request, flash, session
from backend.auth.models import *
from backend.ext.configuration import getDB
from backend.auth.dao import UsuarioDao

param = getDB()
usuario_dao = UsuarioDao(param)


def criaUsuario():
    id = request.form['id']
    nome = request.form['nome']
    senha = request.form['senha']
    usuario = Usuario(id, nome, senha)
    try:
        usuario_dao.salvar(usuario)
        flash('Usuário Criado!')
        return redirect(url_for('index'))
    except:
        flash('Usuário já está registrado!')
        return redirect(url_for('index'))



def login():
    proxima = request.args.get('proxima')
    return render_template('components/auth/login.html', proxima=proxima)


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


def logout():
    if session.get('usuario_logado'):
        session.clear()
        flash('Usuário deslogado!')
        return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))