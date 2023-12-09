#crie uma função que faça a soma de todos os mesus argumentos exceto se o valor de algum for 4 e para ser ignorado
def sem_quatro(*args):
    total = 0
    for numero in args:
        if numero != 4:
            total += numero
            return total
resultado = sem_quatro(1,2,3,4,5)
print(resultado)

