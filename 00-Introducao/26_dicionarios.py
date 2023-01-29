#Criar chaves que não foram pré-definidas
pessoa = {"nome": "Fernando", "idade": 38, "altura": 173}
pessoa.update({"cep": "123456"})
print(pessoa)

#Dicionários são como objetos JSON. Possui índices nomeados
pessoa = { "nome": "Fernando Freitas", "idade": 38, "cep": "77.059-020"}
print (pessoa)

print(pessoa["nome"])

pessoa["nome"] = "Cleilda"

print(pessoa)

#Listas e Dicionários
x = { "nomes": [], "idade": 21} #Dicionário X possui uma lista na posição nomes.
print(x)
print(x["nomes"])

x["nomes"].append("Freitas")
x["nomes"].append("Souza")
print(x)

print(x["nomes"][0]) #Posição 0 da lista nomes do dicionário x

pessoas = [{ "nome": "Fernando", "idade":38, "altura":173 },
           { "nome": "Cleilda", "idade":33, "altura":159 }]

#iterando Lista Pessoas
for pessoa in pessoas:
    print(pessoa)
    print(pessoa.values()) #Imprime lista com somente os valores do dicionário
    print(pessoa.keys()) #Imprime lista com somente as chaves/campos
    print(pessoa.items()) #Imprime uma lista com uma tupla com chave e valor
    print(pessoa["nome"]) #Imprime o valor da chave nome

for pessoa in pessoas:
    print("*" * 100)
    print(pessoa.keys())
