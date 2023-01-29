#Programação Funcional
    #Função Filter (função, iterável)
    #itera sobre uma função lambda e retorna algo
    #filter (lambda parametro: condicao, retorno). Exemplo:
        #filter(lambda pessoas: pessoas['idade'] < 38, pessoas)

x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

x = list(filter(lambda x: x < 18 or x % 2 == 0, x))

print(x)

y = [{'nome': 'Fernando', 'idade': 38}, {'nome': 'Cleilda', 'idade': 33}]

y = list(filter(lambda y: y['idade'] < 38, y))

print(y)
