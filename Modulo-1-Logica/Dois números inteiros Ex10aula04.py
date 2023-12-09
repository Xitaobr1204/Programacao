n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))

inicio = min(n1,n2)
fim = max(n1,n2)

for i in range (inicio, fim + 1):
    print(i, end=' ')