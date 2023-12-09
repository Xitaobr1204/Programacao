# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso 
#o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

controle = True

while controle == True:
    nota = input('Insira uma nota:')

    if int(nota) >= 0 and int(nota) <= 10:
        print('Nota informada é válida.')
        controle = False
    else:
        print('Nota informada inválida.')