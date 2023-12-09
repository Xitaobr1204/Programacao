#Agora crie um programa que utilizando a função random o usuário deve ter 3 chances para adivinhar um numero de 1 a 15.
from random import choice

lista = range(16)
sorteado = choice(lista)
print(sorteado)
tentativa = 0
while tentativa < 3:
    numero = int(input('Tente advinhar o número de 1 a 15: '))
    if numero == sorteado:
        print('Parabéns, você acertou o número!!!')
        tentativa = 3
    else:
        print('Você errou, tente novamente!!!')
        tentativa += 1
    if tentativa == 3:
        print('Suas tentativas acabaram, tente novamente')