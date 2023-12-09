def infinito(*args):
    return args

'''valores = infinito(1,2,3,4,5,6,7,8,9,0)
print(valores)'''

def somatoria(*args):
    aux = 0
    for x in args:
        aux += x
    return aux

f = somatoria(1,2,3,4,5,6,7,8,9)

def media(*args):
    aux = 0
    for x in args:
        aux += x 

    quantidade = len(args)

    media1 = aux/quantidade
    return media1
print(media(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

