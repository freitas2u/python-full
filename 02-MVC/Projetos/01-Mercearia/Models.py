"""
    Camada de modelo, apenas a estrutura das classes
"""

from datetime import datetime

class Categoria:
    """
        Classe de categorias de produtos
    """
    def __init__(self, descricao):
        self.descricao = descricao

class Produto:
    """
        Classe de produtos
    """
    def __init__(self, descricao, preco, categoria):
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria

class Estoque:
    """
        Classe de estoque de produtos
    """
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    """
        Classe de Vendas feitas
    """
    def __init__(self, itens_vendidos: Produto, vendedor, comprador, qtde_vendida, data = datetime.now()):
        self.itens_vendidos = itens_vendidos
        self.vendedor = vendedor
        self.comrpador = comprador
        self.qtde_vendida = qtde_vendida
        self.data = data

class Fornecedor:
    """
        Classe de fornecedor dos produtos
    """
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    """
        Classe de Pessoas/Cliente base (Classe mãe)
    """
    def __init__(self, nome, telefone, cpf, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

class Funcionario(Pessoa):
    """Classe de Funcionário/Vendedor

    Args:
        Pessoa (_type_): _description_
    """
    def __init__(self, clt, nome, telefone, cpf, email, endereco):
        self.clt = clt
        super(Funcionario, self).__init__(nome, telefone, cpf, email, endereco)
