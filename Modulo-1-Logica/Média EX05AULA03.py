# Faça um programa para calcular a média de uma lista de números.

lista_numeros = [10,20,30,40,50] #números

#Variável para soma
soma = 0

#Conte quantos números tem na lista
elementos = 0

for numero in lista_numeros:
    soma += numero
    elementos += 1

#Calcule a média
media = soma / elementos
#Imprima a média
print('A média dos números é:', media)