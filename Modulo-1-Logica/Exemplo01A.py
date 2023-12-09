nome = input('Informe o seu nome:')
idade = input('Informe a sua idade:')

idade_int = int(idade)

if idade_int < 18: #regra 1
    # o código será executado caso a regra seja verdadeira
    print(f'Olá, {nome}. Você é maior de idade')

elif idade_int == 18: #regra 2
    print(f'Olá,{nome}. Você já tem 18 anos. Parabéns!')

elif idade-int == 21: #regra 3
    print(f'Olá,{nome}. Você já pode se candidatar ao cargo de vereador')

else:
    print(f'Olá, {nome}. Você é maior de idade')
