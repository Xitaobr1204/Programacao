#Considere a seguinte lista de números: [2, 5, 8, 11, 14]. Escreva um programa que itere sobre essa lista e exiba cada número elevado ao quadrado.

numeros = [2,5,8,11,14]
#Eleva-los ao quadrado
for numero in numeros:
    quadrado = numero ** 2
    print(f'O quadrado de {numeros} é: {quadrado}')