#O conceito de lista no python é semelhante ao vetor/array em outras linguagens
#Listas são representadas com elementos entre colchetes: [1,2,3,4,5]


nomes = ["Fatima", "Fernando", "Flávia", "Fabrício"]

#imprimir uma lista
print(nomes)

#acessar posição na lista
print(nomes[0])

#obter o tamanho da lista
print(len(nomes))

#alterar o valor em uma posição da lista
nomes[0] = "Freitas"
print(nomes)

#Append (Adiciona um item ao final lista)
nomes.append("Joana")
print(nomes)

#Insert (Adiciona um item ao na posição especificada da lista)
nomes.insert(0, "Maria")
print(nomes)

#Pop (Remove o último valor da lista. Se passar um valor para a função, o elemento removido será o do índice)
nomes.pop()
print(nomes)

#Remove (Remover um valor da lista. Caso exista, mais de uma posição com o mesmo valor, será removida a primeira ocorrência)
nomes.remove("Maria")

#Index (Descobre a posição do elemento na lista)
nomes.index("Freitas")
print(nomes)

nomes = []
while True:
    nome = input("Digite -1 para sair ou cadastre um nome: ")
    if nome == "-1":
        break
    else:
        nomes.append(nome)

print(nomes)

#Sort(Ordenando Listas)
nomes.sort() #Altera a lista atual ordenando em ordem crescente
print(nomes)

nomes.sort(reverse=True) #Altera a lista atual ordenando em ordem decrescente
print(nomes)

sorted(nomes) #Retorna uma nova lista ordenada em ordem crescente
sorted(nomes, reverse=True) #Retorna uma nova lista ordenada em ordem decrescente

#Iterando listas
#Forma comum
for i in range(0, len(nomes)):
    print(i)
    print(nomes[i])

#Recomendação Python
for indice, elemento in enumerate(nomes):
    print(indice) #posição
    print(elemento) #valor

#Matrizes ou Listas de Listas
idades = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print(idades[2][3])

#Iterando Matrizes
for i in range(0,len(idades)):
    print(idades[i]) #For para as linhas. Mostra a linha toda

    for j in range(0, len(idades[i])):
        print(idades[i][j])#For para as colunas. Mostra cada um dos elementos
