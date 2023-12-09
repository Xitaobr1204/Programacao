numero = 1
controle = True

# Condição: a regra de negócio
# Controle: o que faz o laço parar

while controle: #condição
    print(numero)
    numero = numero + 1 

    #Cláusula de controle
    if numero > 7:
        controle = False
else:
    print('Fim.')