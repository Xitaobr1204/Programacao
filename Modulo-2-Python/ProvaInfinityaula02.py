#Faça um programa que solicite ao usuário que digite 10 valores parapreencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.
numeros = []
pares = []
impares = []

for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    numeros.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print("Números Pares:", pares)
print("Números Ímpares:", impares)

numeros_tupla = tuple(pares + impares)

print("Números em Tupla:", numeros_tupla)

qtd_pares = len(pares)
qtd_impares = len(impares)

print("Quantidade de Números Pares:", qtd_pares)
print("Quantidade de Números Ímpares:", qtd_impares)

soma_pares = sum(pares)
soma_impares = sum(impares)

print("Soma dos Números Pares:", soma_pares)
print("Soma dos Números Ímpares:", soma_impares)
