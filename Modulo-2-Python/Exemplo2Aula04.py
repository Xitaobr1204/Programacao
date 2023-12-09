def soma(x,y):
    resultado = x + y
    return resultado


def sub(a,b):
    result = a - b
    if a < b:
        return 'O valor é negativo não vou fazer'
    else:
        return result

valor1 = int(input('Digite o primeiro valor:'))
valor2 = int(input('Digite o segundo valor:'))
print(sub(valor1,valor2))