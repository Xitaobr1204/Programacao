#Pedir um valor ao usuário
valor = float(input('Insira um valor:'))

#Números positivos
if valor > 0:
    print('O valor é positivo.')
#Números negativos
elif valor < 0:
    print('O valor é negativo.')
#Se o valor inserido for zero
elif valor == 0:
    print('O valor inserido é neutro')