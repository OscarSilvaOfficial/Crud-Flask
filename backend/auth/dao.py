from backend.auth.models import *

SQL_USUARIO_POR_ID = 'SELECT id, nome, senha from usuario where id = %s'
SQL_ATUALIZA_USUARIO = 'UPDATE usuairo SET nome=%s, senha=%s where id = %s'
SQL_CRIA_USUARIO = 'INSERT into usuario values (%s, %s, %s)'


class UsuarioDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, usuario):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIA_USUARIO, (usuario.id, usuario.nome, usuario.senha))
        usuario.id = cursor.lastrowid
        self.__db.connection.commit()
        return usuario

    def buscar_por_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID, (id,))
        dados = cursor.fetchone()
        usuario = traduz_usuario(dados) if dados else None
        return usuario


def traduz_usuario(tupla):
    return Usuario(tupla[0], tupla[1], tupla[2])
