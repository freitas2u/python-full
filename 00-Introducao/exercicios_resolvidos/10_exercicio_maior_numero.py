#Receba 3 números inteiros e exiba o maior deles
numero01 = int(input("Informe o primeiro número: "))
numero02 = int(input("Informe o segundo número: "))
numero03 = int(input("Informe o terceiro número: "))

if (numero01 > numero02) and (numero01 > numero03):
    maior = numero01
elif (numero02 > numero01) and (numero02 > numero03):
    maior = numero02
else:
    maior = numero03

print(f"O maior número informado é: {maior}")
