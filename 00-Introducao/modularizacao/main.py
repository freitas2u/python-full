#Modularização é o ato de dividir o seu projeto em módulos (outros arquivos), podendo estes módulos serem usados em outras partes do projeto através de importações.

from funcoes.minha_lib import * #importa tudo
from funcoes.minha_lib import x #importa somente uma variável
from funcoes.minha_lib import x,y #importa somente as duas variáveis
from funcoes.minha_lib import x as x_importado #importa variável colocando um alias
from funcoes.minha_lib import soma_dois_numeros #importa uma função

x = 1
print(x)
print(x_importado)
print(y)
