#Receba 10 valores e exiba a soma de todos eles

#Forma "Normal"
numeros = []
soma = 0

for i in range(0,10):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
    soma += numeros[i]

print(numeros)
print(soma)

#Forma "List Comprehension"
soma = [float(input("Digite um número: ")) for i in range(0, 10)]
print(sum(soma))
