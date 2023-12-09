#Solicitar três números ao usuário
n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Dgite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))

#Encontrar o maior número
maior_numero = max(n1,n2,n3)

#Encontrar o menor número
menor_numero = min(n1,n2,n3)

#Exibir o maior e o menor número
print(f'O MAIOR NÚMERO É: {maior_numero}')
print(f'O MENOR NÚMERO É:{menor_numero}')