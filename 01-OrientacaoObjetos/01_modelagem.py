#pep8
    #Classes com InitCaps
    #Funções com snake_case()

#Atributos de Instância: Só podemos acessar através de uma instância (objeto)
#Atributos de Classe: Não precisamos acessar a instância.
    # Podemos acessar diretamente pela classe
    # Algo que todos os objetos possuemo mesmo valor

class Pessoas:
    possui_olho = True #Atributos da Classe
    possui_boca = True #Atributos da Classe
    raca = "Ser Humano" #Atributos da Classe

    @classmethod #Decorador que define que o método pertence à classe. Precisa receber o cls. Pelo cls podemos modificar atributos, criar atributos
    def metodo_qualquer(cls): #Método da Classe. cls representa a classe
        print("Método Qualquer")

    @classmethod
    def andar(cls):
        cls.pernas = 2 #Criando atributos de Classe pelo cls
        return None

    @staticmethod#Decorador que define que é um método estático. Método utilitário que consegue acessar a classe.
    def e_adulto(idade):
        if idade > 18:
            return True
        else:
            return False

    def __init__(self, nome, idade, cpf):
        #Método que será chamado sempre que uma classe for instanciada
        #self referencia à uma instância. Self é si mesmo
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

        nome_pessoa = nome #Sem self? Não é possível acessar de fora da instância

    def logar_sistema(self):
        #Método de instância
        print(f"{self.nome} está logando no sistema")

pessoa01 = Pessoas("Fernando Freitas de Souza", 38, "12345678901")
pessoa02 = Pessoas("Cleilda Alves Santos Freitas", 33, "98765432109")

print(vars(pessoa01))
print(vars(pessoa02))
print(pessoa01.nome)
print(pessoa02.nome)
pessoa01.logar_sistema()
pessoa02.logar_sistema()

Pessoas.andar()
print(Pessoas.pernas)
