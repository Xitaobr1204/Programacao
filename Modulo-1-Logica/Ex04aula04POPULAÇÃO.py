populacao_a = 80_000
populacao_b = 200_000

#Constante para armazenar a taxa de crescimento
TAXA_A = 0.03 #1.5%
TAXA_B = 0.015 #3%

ano = 0
controle = True


while controle == True:
    populacao_a = populacao_a + (populacao_a*TAXA_A)
    populacao_b = populacao_b + (populacao_b*TAXA_B)



    ano = ano + 1

    if populacao_a > populacao_b:
        controle = False

else:
    print(f'Número de anos: {ano}')



