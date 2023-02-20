#Camada de acesso ao banco de dados (Inclusões, Alterações, Pesquisas, Exclusões)

from model import Pessoa

class PessoaDAL:
    """ DAL da Classe Pessoa

    # Método salvar (cls, pessoa: Pessoa). Salva objeto pessoa no arquivo texto
    # Método ler (self).


    """
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        """Salva Objeto pessoa no arquivo texto

        Args:
            pessoa (Pessoa): Objeto da Classe Pessoa
        """
        with open('pessoas.txt', 'w') as arquivo:
            arquivo.write(pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)

    def ler(self):
        """Lê conteúdo do arquivo texto e retorna um objeto da classe Pessoa

        Returns:
            pessoa: Pessoa
        """
        nome = 'Fernando'
        idade = 38
        cpf = '11111111111'

        pessoa = Pessoa(nome, idade, cpf)

        return pessoa
