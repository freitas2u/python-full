#Receba F para Feminino e M para Masculino e exiba o sexo da Pessoa

sexo = input("Informe 'F' para 'Feminino' ou 'M' para 'Masculino': ")

if sexo.capitalize() == 'F':
    print('Feminino')
elif sexo.capitalize() == 'M':
    print('Masculino')
else:
    print('Sexo inválido')
