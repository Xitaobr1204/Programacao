#Com a mesma função agora mostre cada argumento multiplicado por 4
def mostrar_elementos (*args):
    for x in args:
        print(x*4)
mostrar_elementos(1,2,3,4,5,6,7,8,9,10)