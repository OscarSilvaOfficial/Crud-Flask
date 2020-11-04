class Jogo:
    def __init__(self, jogo, categoria, console, id = None):
        self.id = id
        self.jogo = jogo
        self.categoria = categoria
        self.console = console

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha