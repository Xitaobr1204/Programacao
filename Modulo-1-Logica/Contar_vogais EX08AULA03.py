# Faça um programa para contar quantas vogais existem em uma palavra. 
# Utilize a condicional IF dentro do laço FOR.
palavra = input('DIGITE UMA PALAVRA:')
palavra = palavra.lower()

consoantes = 0

for letra in palavra: 
    if letra in 'bcdfghjklmnpqrstvwxyz':
        consoantes += 1

print('NÚMERO DE CONSOANTES NA PALAVRA:', consoantes)