# Faça um programa para verificar se um número é primo. Utilize a 
# condicional IF dentro do laço FOR.
numero = int(input('INSIRA UM NÚMERO:'))

if numero <= 1:
    print(numero, 'não é um número primo.')
else:
    eh_primo = True
for  i in range (2, numero):
    if numero % i == 0:
        eh_primo = False

    break

if eh_primo:
    print(numero,'é um número primo.')
else:            
    print(numero,'não é um número primo')