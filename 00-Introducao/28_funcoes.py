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

    Args (argumentos) é uma tupla contendo todos os números recebidos separados por vírgula

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
    Função que faz alguma coisa

    Kwargs é um dicionário contendo tudo o que recebeu onde:
        o parâmetro se torna a chave
        o valor do parâmetro se torna o valor do dicionário
    """

    #a linha abaixo testa a existência de um parâmetro dentro dos kwargs
    x = kwargs.get('teste1')
    return kwargs

soma_algo(teste1 = 1, teste2 = 2, teste3 = 3)
