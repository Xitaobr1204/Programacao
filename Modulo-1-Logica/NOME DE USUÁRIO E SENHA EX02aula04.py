# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as 
#informações.

controle = True

while controle == True:
    usuario = input('INSIRA UM USUÁRIO:')
    senha = input('INSIRA UMA SENHA:')

    if usuario == senha:
        print('Usuário e senha não podem ser iguais.')
    else:
        print('Usuário e senha válidos.')
    controle = False
    