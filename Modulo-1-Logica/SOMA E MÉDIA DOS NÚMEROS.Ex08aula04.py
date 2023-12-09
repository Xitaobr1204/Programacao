numeros = []
soma = 0

for i in range(5):
    numero = float(input(f'Digite o {i + 1}º número:'))
    numeros.append(numero)
    soma += numero

    media = soma / 5

    print(f'Soma dos números:{soma}')
    print(f'Média dos números:{media}')