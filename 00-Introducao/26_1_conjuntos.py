#Conjuntos que não possuem registros repetidos
#Conjuntos são representados com elementos entre chaves: {1, 2, 3, 4, 5}
x = ['Fernando', 1, 1, 2, 2, 3, 4, 5]

#Pode-se converter uma lista em um conjunto através do comando set
x = set(x)
print(x)

#Pode-se fazer todas as operações matemáticas com conjuntos:

#União (Todos os elementos não repetidos de todos os conjuntos)
x = {1, 2, 3}
y = {4, 5, 6}
z = x.union(y)
print(z)

#Intersecção (Somente os elementos que aparecem em todos os conjuntos)
x = {1, 2, 3, 4}
y = {4, 5, 6}
z = x.intersection(y)
print(z)

#Diferença (Retira do conjunto o que aparecer nos outros conjuntos)
x = {1, 2, 3, 4, 5}

#Diferença Simétrica (Semelhante ao union, mas a intersecção não é mostrada)
x = {1, 2, 3, 4, 5}
y = {5, 6, 7, 8, 9, 10}
z = x.symmetric_difference(y)
print(z)
