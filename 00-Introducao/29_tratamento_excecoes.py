#try e except
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

try:
    print(n1/n2)
    print(n3)
except Exception as error:
    print(error)

#raise e assert
raise ValueError("Deu muito ruim")

#Quando usar o raise?
#normalmente usado quando criamos bibliotecas (libraries)

#Quando queremos forçar uma assertividade, se ela não der certo, vai mostrar mensagem
x = -2
assert x > 0, "Deu bem ruim"
