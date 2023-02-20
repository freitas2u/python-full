# Camada de Visão (View)
    # É a camada de apresentação, uma tela, uma página. É responsável pela interface do projeto
    # A View (Tela/Página do cliente) faz uma requisição ao Control

from controller import PessoaController

while True:
    decisao = int(input('Digite 1 para salvar uma pessoa, digite 2 para ver a pessoa salva e 3 para sair'))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input("Digite o nome")
        idade = int(input("Digite a idade"))
        cpf = input("Digite o cpf")

        if PessoaController().cadastrar(nome, idade, cpf):
            print("Usuário Cadastrado com Sucesso")
        else:
            print("Digite valores válidos")
