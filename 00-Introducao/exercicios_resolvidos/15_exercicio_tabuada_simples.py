#Receba um número do usuário e mostre a tabuada desse número

numero = int(input("Digite um número para exibir a tabuada: "))

i = 1

while i <= 10:
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
    i += 1
