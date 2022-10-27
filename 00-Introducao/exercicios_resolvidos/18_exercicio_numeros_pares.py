"""
Receba um número e mostre todos os números pares de 0 até o número digitado
"""

numero_digitado = int(input("Informe um número: "))

i = 0

while i <= numero_digitado:
    if i % 2 == 0:
        print(i)
    i += 1
