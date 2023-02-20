"""
    Camada DAO. Camada de acesso ao banco de dados (Inclusões, Alterações, Pesquisas, Exclusões)
"""

class DaoCategoria:
    """
        DAO Categoria. Salvar e Ler.
    """
    @classmethod
    def salvar(cls, categoria):
        """
            Salva Objeto pessoa no arquivo texto

        Args:
            categoria (string): Descrição da Categoria
        """
        with open("categorias.txt", "a", encoding='UTF-8') as arquivo:
            arquivo.writelines(categoria)
            arquivo.writelines("\n")

    @classmethod
    def ler(cls):
        """
            Lê conteúdo do arquivo texto e imprime o conteúdo lido na tela
        """
        with open("categorias.txt", "r", encoding='UTF-8') as arquivo:
            cls.categoria = arquivo.readlines()

        print(cls.categoria)

DaoCategoria().salvar("Frutas")
DaoCategoria().salvar("Verduras")
DaoCategoria().salvar("Legumes")
DaoCategoria().ler()
