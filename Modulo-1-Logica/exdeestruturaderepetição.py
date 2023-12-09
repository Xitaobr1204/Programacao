palavra = 'vicissitudes'
numero_vogais = 0

for letra in palavra:
    if letra in 'aeiou':
        numero_vogais = numero_vogais + 1 #incremento

print(f'A palavra {palavra} tem {numero_vogais} vogais.')


