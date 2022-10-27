for i in range (0, 5): #O segundo parâmetro na função range é "não inclusivo"
    print(i)

for i in range(0, 100, 2): #O terceiro parâmetro é o step, ou seja, o incremento vai de 2 em 2
    print(i)

for i in range(100, 0, -1): #Decrescente, decrementando de 1 em 1
    print(i)

x = [2,7,'x','z',45]
for i in x: #Percorrendo um iterável (lista)
    print(i)

#for aninhado
for i in range(0,3):
    for j in range (0,3):
        print(f"i = {i} j = {j}")
