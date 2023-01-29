#pep8
    #Classes com InitCaps
    #Funções com snake_case()

class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def logar_sistema(self):
        print(f"{self.nome} está logando no sistema")

pessoa01 = Pessoas("Fernando Freitas de Souza", 38, "12345678901")
pessoa02 = Pessoas("Cleilda Alves Santos Freitas", 33, "98765432109")

print(vars(pessoa01))
print(vars(pessoa02))
print(pessoa01.nome)
print(pessoa02.nome)
pessoa01.logar_sistema()
pessoa02.logar_sistema()
