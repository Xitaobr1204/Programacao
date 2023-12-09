dados={
    'nome': 'Washington',
    'cep': 30421565,
    'idade': 21,
    'pais': 'Brasil'
}

'''print(list(dados))
print(dados)
print(len(dados))'''
print(dados)
#print(dados['nome'])

listaChaves = list(dados)
for x in listaChaves:
    print(dados[x])

del dados['cep']
print(dados)

print('cep' not in dados)

print(iter(dados))
print(dados.get('cep','não achei'))

dados2 = dados.items()
print(dados2)

for chave, valor in dados2:
    print(f'chave:{chave} /// valor:{valor}')


dados.pop('nome')
print(dados)

dados3= {  'sexo':'masculino', 'altura': 1.70, 'cep': 30421565  }
dados.update(dados3)
print(dados3)