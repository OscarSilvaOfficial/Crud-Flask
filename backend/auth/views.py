from flask import *
from .models import *
from ext.configuration import *


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