#Serialização de Objetos
    #Pegar algo que está em memória e torná-lo persistente (banco, arquivo) exatamente como ele é

import pickle

lista = [1, 2, 3, 4]

serializacao = pickle.dumps(lista) #serialização do objeto lista
desserializacao = pickle.loads(serializacao)
print(serializacao)
print(desserializacao)

dicionario = {'nome': "Fernando", 'idade': 38}
dicionario_serializado = pickle.dumps(dicionario)
dicionario_desserializado = pickle.loads(dicionario_serializado)
print(dicionario_serializado)
print(dicionario_desserializado)

with open('arquivo.pkl', 'ab') as arquivo:
    pickle.dump(lista, arquivo)

with open('arquivo.pkl', 'rb') as arquivo:
    retornou = pickle.load(arquivo)

print(retornou)

class Pessoa:
    nome = "Fernando"
    idade = 38

with open('arquivo.pkl', 'wb') as arquivo:
    pickle.dump(Pessoa, arquivo)

with open('arquivo.pkl', 'rb') as arquivo:
    retornou = pickle.load(arquivo)
    print(retornou.idade)


class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoas('Fernando', 40)

with open('arquivo.pkl', 'ab') as arquivo:
    pickle.dump(Pessoa, arquivo)

with open('arquivo.pkl', 'rb') as arquivo:
    retornou = pickle.load(arquivo)
    print(retornou.nome)
