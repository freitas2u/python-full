#Escreva um programa onde o usuário digite duas notas e mostre a média das duas notas

from statistics import median


nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))

media = (nota01 + nota02) / 2

print(f"Sua média é: {media}")
