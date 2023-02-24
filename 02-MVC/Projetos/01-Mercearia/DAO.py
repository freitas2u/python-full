"""
Camada DAO. Camada de acesso ao banco de dados (Inclusões, Alterações, Pesquisas, Exclusões)
"""

from models import *

class DaoCategoria:
    """
    DAO Categoria.

    Métodos: salvar(categoria) e ler().
    """
    @classmethod
    def salvar(cls, categoria):
        """
        Salva Objeto categoria no arquivo texto

        Args:
            categoria (string): Descrição da Categoria
        """
        with open("categorias.txt", "a", encoding='UTF-8') as arquivo:
            arquivo.writelines(categoria)
            arquivo.writelines("\n")

    @classmethod
    def ler(cls):
        """
        Lê conteúdo do arquivo texto e retorna uma lista de categorias

        Returns:
            cat: lista de categorias
        """
        with open("categorias.txt", "r", encoding='UTF-8') as arquivo:
            cls.categoria = arquivo.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []
        for descricao in cls.categoria:
            cat.append(Categoria(descricao))

        return cat

class DaoVenda:
    """
    DAO Venda.

    Métodos: salvar(venda) e ler().
    """
    @classmethod
    def salvar(cls, venda: Venda):
        """
        Salva Objeto venda no arquivo texto

        Args:
            Venda(itens, vendedor, comprador, qtde)
            itens -> Objeto da classe Produto
            vendedor -> nome do Vendedor
            comprador -> nome do Comprador
            qtde -> Quantidade Vendida
        """
        with open("venda.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.writelines(venda.itens.descricao + "|" + venda.itens.preco + "|" + venda.itens.categoria + "|" + venda.vendedor + "|" + venda.comprador + "|" + str(venda.qtde) + "|" + venda.data)
            arquivo.writelines("\n")

    @classmethod
    def ler(cls):
        """
        Lê conteúdo do arquivo texto e retorna uma lista de listas de Vendas

        Returns:
            vend: lista de vendas realizadas
        """
        with open("venda.txt", "r", encoding="UTF-8") as arquivo:
            cls.venda = arquivo.readlines()

        cls.venda = list(map(lambda x: x.replace("\n", ""), cls.venda))
        cls.venda = list(map(lambda x: x.split("|"), cls.venda))
        print(cls.venda)

        vend = []
        for i in cls.venda:
            vend.append(Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))

        return vend

class DaoEstoque:
    """
    DAO Estoque.

    Métodos: Salvar e Ler.
    """
    @classmethod
    def salvar(cls, produto: Produto, qtde):
        """
        Salva Objeto produto no arquivo texto e a sua quantidade atual em estoque

        Args:
            produto (Produto): Objeto da classe Produto:
                descrição ->
                preço ->
                categoria ->
            qtde (int): Quantidade atual no estoque
        """
        with open("estoque.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.writelines(produto.descricao + "|" + produto.preco + "|" + produto.categoria + "|" + str(qtde))
            arquivo.writelines("\n")

    @classmethod
    def ler(cls):
        """
        Lê conteúdo do arquivo texto e retorna uma lista de produtos em estoque

        Returns:
            est: Lista de produtos em estoque
        """
        with open("estoque.txt", "r", encoding="UTF-8") as arquivo:
            cls.estoque = arquivo.readlines()

        cls.estoque = list(map(lambda x: x.replace("\n", ""), cls.estoque))
        cls.estoque = list(map(lambda x: x.split("|") ,cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produto(i[0], i[1], i[2]), i[3]))

        return est

class DaoFornecedor:
    """
    DAO Fornecedor.

    Métodos: Salvar e Ler.
    """
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        """
        Salva Objeto fornecedor no arquivo texto

        Args:
            fornecedor (Fornecedor): Objeto da classe Fornecedor:
                nome ->
                cnpj ->
                telefone ->
                categoria ->
        """
        with open("fornecedores.txt","a",encoding="UTF-8") as arquivo:
            arquivo.writelines(fornecedor.nome + "|" + "" + fornecedor.cnpj + "|" + fornecedor.telefone + "|" + fornecedor.categoria)
            arquivo.writelines("\n")

    @classmethod
    def ler(cls):
        """
        Lê conteúdo do arquivo texto e retorna uma lista de Fornecedores

        Returns:
            forn: Lista de produtos em estoque
        """
        with open("fornecedores.txt", "r", encoding="UTF-8") as arquivo:
            cls.fornecedores = arquivo.readlines()

        cls.fornecedores = list(map(lambda x: x.replace("\n", ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split("|"), cls.fornecedores))
        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))

        return forn

class DaoPessoa:
    """
    DAO Pessoa.

    Métodos: Salvar e Ler.
    """
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        """
        Salva um cliente (Objeto pessoa) no arquivo texto

        Args:
            pessoa (Pessoa):
                nome ->
                telefone ->
                cpf ->
                email ->
                endereco ->
        """
        with open("clientes.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.writelines(pessoa.nome + "|" + pessoa.telefone + "|" + pessoa.cpf + "|" + pessoa.email + "|" + pessoa.endereco)
            arquivo.writelines("\n")

    @classmethod
    def ler(cls):
        """
        Lê conteúdo do arquivo texto e retorna uma lista de clientes (Pessoas)

        Returns:
            cli: Lista de clientes cadastrados
        """
        with open("clientes.txt", "r", encoding="UTF-8") as arquivo:
            arquivo.readlines()

        cls.clientes = list(map(lambda x: x.replace("\n", ""), cls.clientes))
        cls.clientes = list(map(lambda x: x.split("|"), cls.clientes))

        cli = []
        for i in cls.clientes:
            cli.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return cli

class DaoFuncionario:
    """
    DAO Funcionario.

    Métodos: Salvar e Ler.
    """
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        """
        Salva funcionario (Objeto pessoa) no arquivo texto

        Args:
            pessoa (Pessoa):
                nome ->
                telefone ->
                cpf ->
                email ->
                endereco ->
        """
        with open("funcionarios.txt", "a", encoding="UTF-8") as arquivo:
            arquivo.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.telefone + "|" + funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arquivo.writelines("\n")

    @classmethod
    def ler(cls):
        """
        Lê conteúdo do arquivo texto e retorna uma lista de funcionários (Pessoas)

        Returns:
            func: lista de funcionários (Objeto pessoa) cadastrados
        """
        with open("funcionarios.txt", "r", encoding="UTF-8") as arquivo:
            cls.funcionarios = arquivo.readlines()

        cls.funcionarios = list(map(lambda x: x.replace("\n", ""), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split("|"), cls.funcionarios))

        func = []
        for i in cls.funcionarios:
            func.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return func
