#Geradores. Tema complexo, quando precisar ir até a aula 59 do módulo de introduçaõ

from pympler.asizeof import asizeof

numero = 50000000000
lista_inteiros = [1,2]

print(asizeof(lista_inteiros)) #Mostra o valor em Bits armazenado na memória do PC

def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i*2)
    return lista_dobro

x = asizeof(dobro(range(0,100)))
print(x)


def dobro2(lista):
    return 1

x = asizeof(dobro2([1,2]))
print(x)
