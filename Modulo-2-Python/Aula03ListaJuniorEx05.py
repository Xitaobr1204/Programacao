#crie uma lista de tuplas com o dicionario da questao dois exibindo a chave e o valor.
dicionario = {'Nome':'Washington',
              'Sobrenome':'Alves',
              'Idade':21,
              'Aniversário': '25 de maio'
}
for chave, valor in dicionario.items():
    print(f'chave:{chave} /// valor:{valor}')