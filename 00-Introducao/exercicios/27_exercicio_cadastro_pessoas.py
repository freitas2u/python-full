#Faça um programa que o usuário possa cadastrar n pessoas,
#Armazenando seu nome, idade e altura
#Ao digitar 1, ele cadastra a pessoa, ao digitar 2 ele deve sair

pessoas = []

while True:
    opcao = int(input("Digite '1 para cadastrar' uma pessoa ou '2' para 'Sair': "))

    if opcao == 2:
        break
    elif opcao != 1 and opcao != 2:
        print("Opção Inválida. Digite Novamente.")
        continue
    else:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = int(input("Altura: "))

        pessoa = {"nome": nome, "idade": idade, "altura": altura}

        pessoas.append(pessoa)

print(pessoas)
