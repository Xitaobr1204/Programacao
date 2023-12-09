consoantes = 'bcdfghjklmnpqrstvwxyz'
vogais = 'aeiou'

palavra = 'vicissitudes'
numero_consoantes = 0
numero_vogais = 0
for letra in palavra:
    if letra in consoantes:
        numero_consoantes = numero_consoantes + 1 #incremento
    if letra in vogais:
        numero_vogais = numero_vogais + 1    

print(f'A palavra {palavra} tem {numero_consoantes} consoantese e {numero_vogais} vogais.')
