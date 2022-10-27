"""
Receba 04 nota de um aluno e exiba se:
    - ele foi aprovado (nota maior ou igual a 6)
    - ficou de recuperação (nota maior ou igual a 4)
    - ele foi reprovado (nota menor que 04)
"""

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))
nota04 = float(input("Digite a quarta nota: "))

media = (nota01 + nota02 + nota03 + nota04) / 4

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Em Recuperação")
else:
    print("Reprovado")
