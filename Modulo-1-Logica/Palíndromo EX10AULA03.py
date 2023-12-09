#  Faça um programa para verificar se uma palavra é um palíndromo. 
# Exemplo: ‘amor’ = ‘roma’ (NÃO É) / ‘arara’ = ‘arara’ (É PALÍNDROMO).

palavra = input('INSIRA UMA PALAVRA:')
palavra = palavra.lower()

if palavra == palavra[::-1]:
    print('A PALAVRA É UM PALÍNDROMO')
else:
    print('A PALAVRA NÃO É UM PALÍNDRMO')