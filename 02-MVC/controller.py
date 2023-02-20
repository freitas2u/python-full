#Camada Controller
    #Camada onde está a regra de negócio do sistema. Normalmente a lógica/regra de negócio fica na camada de controle.
from dal import PessoaDAL
from model import Pessoa

class PessoaController:
    @classmethod
    def cadastrar(cls,nome, idade, cpf):
        """Cadastrar uma pessoa no banco de dados

        Args:
            nome (str): Nome da Pessoa
            idade (int): Idade da Pessoa
            cpf (str): CPf da pessoa

        Returns:
            bool: True (Cadastrou) ou False (Não Cadastrou)
        """
        if len(nome) > 2 and (idade > 0 and idade < 200) and len(cpf) == 11:
            pessoa = Pessoa(nome, idade, cpf)
            try:
                PessoaDAL().salvar(pessoa)
                return True
            except:
                return False
        else:
            return False


