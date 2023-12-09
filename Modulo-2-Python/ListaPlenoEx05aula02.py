#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
numeros = []
par = []
impar = []

for i in range(20):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))
    numeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

#Imprimir os números na tela
print('Números digitados:', numeros)
print('Números pares:', par)
print('Números ímpares:', impar)