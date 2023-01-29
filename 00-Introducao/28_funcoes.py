"""
    Arquivo que possui várias funções que podem ou não receber valor, executar comandos e retornar ou não algum valor
"""

#Criar uma função
def minha_funcao():
    """
    Função simples para exibir dois prints
    """
    print("Oi")
    print("Tudo bem?")

#Chamar a função Criada
minha_funcao()

def soma_numeros(n_1, n_2):
    """
    Função que soma dois números

    Args:
        n1 (inteiro ou float): Primeiro número
        n2 (inteiro ou float): Segundo número

    Returns:
        inteiro ou float: Retorna a soma de ambos
    """
    return n_1 + n_2

SOMA = soma_numeros(2, 3)
print(SOMA)

def soma_numeros_indefinidos(*args):
    """
    Função que somará quantos números forem passados

    Args (argumentos) é uma tupla contendo todos os valores recebidos separados por vírgula. O nome args pode ser substituído por qualquer coisa desde que o "*" esteja antes do parâmetro

    Returns:
        Número: Somatório de todos os números contigos no parâmetro *args
    """
    soma = 0
    for i in args:
        soma += i
    return soma

SOMA = soma_numeros_indefinidos(1, 2, 3, 4, 5, 6, 7, 8)
print(SOMA)

def soma_algo(**kwargs):
    """
    Função que faz alguma coisa e retorna

    Kwargs é um dicionário contendo tudo o que recebeu onde:
        o parâmetro se torna a chave
        o valor do parâmetro se torna o valor do dicionário
    """

    #a linha abaixo testa a existência de um parâmetro dentro dos kwargs
    x = kwargs.get('teste1')

    #a linha abaixo pega o valor da chave existente no Kwargs
    x = kwargs['teste1']
    y = kwargs['teste2']
    z = kwargs['teste3']
    return kwargs

soma_algo(teste1 = 1, teste2 = 2, teste3 = 3)

def soma_valores(n1, n2):
    soma = n1 + n2

    #a linha abaixo mostra como retornar vários valores
    return soma, n1, n2

#Desestruturação. Soma terá o primeiro retorno, n1 o segundo e n2 o terceiro
soma, n1, n2 = soma_valores(1, 2)

