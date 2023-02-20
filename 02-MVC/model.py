# Camada de Modelo (Model)
    # É a camada responsável por representar, sob a forma de classes, os dados do sistema, sua estrutura

    # As classes descritas na camada model, podem ou não serem representações das tabelas do banco de dados

class Pessoa:
    """
    Classe Pessoa
    """
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
