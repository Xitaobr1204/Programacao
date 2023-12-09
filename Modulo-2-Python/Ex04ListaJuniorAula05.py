#Crie a função que calcule a media de todos os meus argumentos
def calculo_media (*args):
    if not args:
        return 0
    return sum(args) / len(args)

media = calculo_media(1,2,3,4,5)
print(media)