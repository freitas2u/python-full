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
    print(pessoa["nome"])
