#Programação Funcional.
    #Funções Lambda:
    #Possuem Sintax mais "curta"
    #Sempre retornam algo
    #Não necessariamente precisa ser declarada

x = lambda: 10 #Retorna o valor 10, mesmo sem a palavra reservada "return"
print(x())

# a linha abaixo mostra o recebimento de parâmetros pela função lambda
x = lambda nome, idade: print(f"nome = {nome}, idade = {idade}")
x('Fernando', 20)

# a função lambda também pode receber args (tupla) e kwargs(dicionário)
x = lambda *idade: print(idade)
x(1,2,3,4,5,6,7,8,9,10)

x = lambda **pessoa: print(pessoa)
x(pessoa = {
    "nome" : 'Fernando',
    "idade" : 38,
    "altura" : 173
    }
)
