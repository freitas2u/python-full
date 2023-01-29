#Adicione o conteúdo da variável i na lista x, para cada valor iteração do for
#O Código abaixo se interpreta da seguinte forma:
# Adicione o valor i na variável x para cada iteração do for. Sendo x, uma lista
x = [i for i in range(0, 10)]

print(x)


# Adicione o valor i na variável x para cada iteração do for, se i for > 4
x = [i for i in range(0,10) if i > 4]
print(x)
