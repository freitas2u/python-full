"""
Escreva um programa que receba notas de um aluno (0 - 10), caso a nota digitada esteja fora desse intervalo, peça para digitar novamente. Caso a nota seja válida, exibir uma mensagem e sair do laço
"""

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print(f"Nota {nota} inválida. Digite novamente")
        continue
    else:
        print(f"Nota {nota} registrada com sucesso")
        break
