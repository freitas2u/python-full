"""
Defina um usuário e senha e depois verifique se o login do usuário é válido
"""

usuario = "freitas"
senha = str(123456)

while True:
    usuario_informado = input("Informe um usuário: ")
    senha_informada = input("Informe uma senha: ")

    if usuario_informado == usuario and senha_informada == senha:
        print("Usuário autenticado")
        break
    else:
        print("Usuário não autenticado. Confirme login e senha")
        continue
