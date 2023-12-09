#Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
respostas = []

perguntas = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?',
    'Já trabalhou com a vítima?'
]

for pergunta in perguntas:
    resposta = input(pergunta)
    if resposta.lower() == 'sim':
        respostas.append(1)
    else:
        respostas.append(0)

quantidade_sim = respostas.count(1)

if quantidade_sim == 2:
    print('Classificação suspeita.')
elif 3 <= quantidade_sim <= 4:
    print('Cúmplice do crime.')
elif quantidade_sim == 5:
    print('Assassino.')
else:
    print('Inocente.')