#Receba um número e mostre a tabuada completa dele usando o laço for

numero = int(input("Informe um número: "))

for i in range(1,11):
    print(f"{numero} * {i} = {i * numero}")
