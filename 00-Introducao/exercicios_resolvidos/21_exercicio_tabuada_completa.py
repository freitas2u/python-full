#Mostra a tabuada completa de todos os números entre 1 e 10, usando for aninhado

for i in range(1, 11):
    print(f"Tabuada do {i}")
    for j in range (1, 11):
        print(f"{i} * {j} = {i * j}")
    print(f"Fim tabuada do {i}")
