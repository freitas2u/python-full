#Manipulação de Arquivos:
    #arquivo = open('nome_do_arquivo.extensão', modo)
        #modo pode ser:
            #r = ler o conteúdo (Read)
            #w = escrever apagando todo o conteúdo (write)
            #a = escrever adicionando (append)
    #arquivo.write(texto). Escreve no arquivo
    #resultados = arquivo.readlines(). Lê todo o conteúdo do arquivo

arquivo = open('pessoas.txt', 'a')
i = 0
while True:
    arquivo.write(input('Digite o nome:') + " " +input("Digite a idade: ") + "\n")
    i += 1
    if i == 4:
        break

arquivo = open('pessoas.txt', 'r')
linhas_arquivo = arquivo.readlines()
lista_linhas = []

for linha in linhas_arquivo:
    #print(linha) #Mostar linha a linha
    lista_linhas.append(linha.split())

print(lista_linhas[0][1])
arquivo.close()


#usando arquivos como contexto. Fechamento automático do arquivo
with open('pessoas.txt', 'r') as arquivo:
    x = arquivo.read()
    print(x)
