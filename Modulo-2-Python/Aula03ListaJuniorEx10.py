#Troque o elemento “Bob” para “Paulo”
dicionario = {
    "frutas": ["maçã", "banana", "laranja"],
    "numeros": [1, 2, 3, 4, 5],
    "pessoas": ["Alice", "Bob", "Carol"]
}
nome = dicionario['pessoas'][1] = 'Paulo'

print(nome)