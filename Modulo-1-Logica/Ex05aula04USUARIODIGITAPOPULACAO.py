valor_lido_a = input('Informe a populacao A: ')
valor_lido_b = input('Informe a populacao B: ')

populacao_a = float(valor_lido_a)
populacao_b = float(valor_lido_b)

#Constante para armazenar a taxa de crescimento
taxa_lida_a = input('Informe a taxa A (%): ')
taxa_lida_b = input('Informe a taxa B (%): ')

TAXA_A = float(taxa_lida_a) / 100
TAXA_B = float(taxa_lida_b) / 100

ano = 0 
controle = True

while controle == True:
    populacao_a = populacao_a + (populacao_a*TAXA_A)
    populacao_b = populacao_b + (populacao_b*TAXA_B)

    ano = ano + 1

    if populacao_a >= populacao_b:
        controle = False

else:
    print(f'Número de anos: {ano}')
