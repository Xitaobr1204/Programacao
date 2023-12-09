numero = 7
contador = 0

for n in range(1, numero+1):
    if numero % n == 0:
        contador = contador + 1 
else:
    print(f'{numero} é primo' if contador == 2 else f'{numero} não é primo.')