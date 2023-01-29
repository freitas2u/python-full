#Adicionar valores em uma lista
x = []
for i in range(0, 10):
    if i % 2 ==0:
        x.append(i)

#Adicionar valores em uma lista com list comprehension
x = [i for i in range(0,10) if i % 2 == 0]

#Não existe encapsulamento no Python
