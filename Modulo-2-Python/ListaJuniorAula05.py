#crie uma função com 10 argumentos e mostre cada um na tela
def mostrar_elementos (*args):
    for x in args:
        print(x)
mostrar_elementos(1,2,3,4,5,6,7,8,9,10)