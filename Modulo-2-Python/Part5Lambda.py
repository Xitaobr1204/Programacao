#Adição
x = lambda a,b: a+b
print(x(3,4))
#Subtração
x = lambda a,b: a-b
print(x(3,4))
#Multiplicação
x = lambda a,b: a*b
print(x(3,4))
#Divisão
x = lambda a,b: a/b
print(x(3,4))
#Elevado ao quadrado
quadrado = lambda x: x**2
quadrado_input = int(input('Insira um número qualquer: '))
print(quadrado_input**2)
#Par e ímpar
x = lambda a,b: a+b
p = int(input('Insira um número: '))
if p%2 == 0:
    print('par')
else:
    print('impar')

