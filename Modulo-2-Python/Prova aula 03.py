numero = int(input('DIGITE UM NÚMERO INTEIRO ENTRE 1 E 10 PARA VISUALIZAR SUA TABUADA:'))

if  1 <= numero <= 10:
    print(f'Tabuada de {numero}:')

    for i in range (1,11):
        resultado = numero * i
        print (f'{numero} X {i} = {resultado}')
else:
    print('NÚMERO FORA DO PERMITIDO. INSIRA UM NÚMERO VÁLIDO')