#Utilizando o metodo get( ) retorne o valor da chave “Uva” da questão anterior.
#obs: deve declarar um novo dicionario
sacolao = {
    "Maçã": 3,
    "Banana": 6,
    "Laranja": 4,
    "Pêra": 5,
    "Uva": 2,
    "Abacaxi": 1,
    "Melancia": 7,
    "Morango": 8
}
valoruva = sacolao.get('Uva')
dicionarionovo = {'Uva': valoruva}

print("Valor da chave 'Uva':", valoruva)
print("Novo dicionário com a chave 'Uva':", dicionarionovo)