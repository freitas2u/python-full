#Camada Controller
    #Camada onde está a regra de negócio do sistema.

from datetime import datetime
from models import *
from dao import *

class ControllerCategoria:
    """
    Regras de negócio da Categoria

    cadastraCategoria (novaCategoria)

    """
    def cadastra_categoria(self, nova_categoria):
        """
        Insere uma categoria no arquivo texto através da DaoCategoria

        Args:
            nova_categoria (str): Descrição da Categoria
        """
        existe = False
        categorias = DaoCategoria.ler()

        for i in categorias:
            if i.descricao == nova_categoria:
                existe = True
                break

        if not existe:
            DaoCategoria.salvar(nova_categoria)
            print("Categoria cadastrada com sucesso")
        else:
            print(f"A Categoria {nova_categoria} já existe")

    def remover_categoria(self, categoria_existente):
        categorias = DaoCategoria.ler()

        categoria = list(filter(lambda categorias: categorias.descricao == categoria_existente, categorias))

        if len(categoria) <= 0:
            print(f"A categoria {categoria_existente} não existe")
        else:
            for i, categoria in enumerate(categorias):
                if categoria.descricao == categoria_existente:
                    del categorias[i]
                    break

            print("Categoria removida com sucesso")

            with open("categorias.txt", "w", encoding="UTF-8") as arquivo:
                for i in categorias:
                    arquivo.writelines(i.descricao)
                    arquivo.writelines("\n")

    def alterar_categoria(self, categoria_existente, nova_categoria):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.descricao == categoria_existente, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.descricao == nova_categoria, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(nova_categoria) if (x.descricao == categoria_existente) else(x), x))
                print("Alteração realizada com sucesso")
            else:
                print(f"Categoria {nova_categoria} já existe")
        else:
            print(f"Categoria {categoria_existente} não existe")

        with open("categorias.txt", "w", encoding="UTF-8") as arquivo:
            for i in x:
                arquivo.writelines(i.descricao)
                arquivo.writelines("\n")

    def mostrar_categoria(self)            :
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print("Categorias Vazias")
        else:
            for i in categorias:
                print(f"Categoria: {i.descricao}")

a = ControllerCategoria()
a.mostrar_categoria()
