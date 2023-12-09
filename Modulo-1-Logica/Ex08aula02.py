#Inserir o preço dos três produtos
p1 = float(input('DIGITE O PREÇO DO PRIMEIRO PRODUTO:'))
p2 = float(input('DIGITE O NÚMERO DO SEGUNDO PRODUTO:'))
p3 = float(input('DIGITE O NÚMERO DO TERCEIRO PRODUTO:'))

#Encontrar produto mais barato
produto_barato = (p1,p2,p3)

#Verifica o produto mais barato e te indica
if produto_barato == p1:
    print('VOCÊ DEVE COMPRAR O PRIMEIRO PRODUTO.')
elif produto_barato == p2:
    print('VOCÊ DEVE COMPRAR O SEGUNDO PRODUTO.')
else:
    print('VOCÊ DEVE COMPRAR O TERCEIRO PRODUTO.')
