#Código com "problema"
class VendedorErro:
    def falar(self):
        print("Estou falando")

    def andar(self):
        print("Estou andando")

    def vender(self):
        print("Estou vendendo")

class ClienteErro:
    def falar(self):
        print("Estou falando")

    def andar(self):
        print("Estou andando")

    def comprar(self):
        print("Estou comprando")

#Código com Herança
class Pessoa: #Super Classe/Classe Mãe/Base
    def falar(self):
        print("Estou falando")

    def andar(self):
        print("Estou andando")

class Cliente(Pessoa):
    def comprar(self):
        print("Estou Comprando")

    def falar(self): #Sobrepondo método da SuperClasse
        super().falar() #Executa o médoto falar da SuperClasse
        print("Estou Gritando")

class Vendedor(Pessoa):
    def vender(self):
        print("Estou Vendendo")

cliente = Cliente()
cliente.falar() #Vai exibir o conteúdo do método da classe filha


