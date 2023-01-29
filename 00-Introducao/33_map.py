#Programação Funcional
    #Função map (função, iterável)
    #itera sobre uma função lambda e retorna algo
    ##Aplica mudanças em uma determinada lista



x = [i for i in range(12, 26)]
x = list(map(lambda x:10 if x < 18 else (x), x))
print(x)


y = [{'nome': 'Fernando', 'idade': 38}, {'nome': 'Cleilda', 'idade': 33}]
y = list(map(lambda y: 10 if y['idade'] < 38 else (y), y))
print(y)

z = [{'nome': 'Fernando', 'idade': 38}, {'nome': 'Cleilda', 'idade': 33}]
z = list(map(lambda z: {'nome': z['nome'], 'idade': ['menor que 40']}  if z['idade'] < 40 else (z), z))
print(z)
