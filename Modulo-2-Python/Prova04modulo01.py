#Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número inteiro(tecle 0 para encerrar):"))

    if numero == 0:
        break
    soma += numero
    quantidade += 1

    print ('Quantidade de numeros digitados:', quantidade)
    print('Soma dos números digitados:', soma) 

