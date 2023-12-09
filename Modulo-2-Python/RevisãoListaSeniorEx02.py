meu_dicionario = {
    "frutas_lista": ["maçã", "banana", "laranja"],
    "numeros_tupla": (1, 2, 3),
    "cores_lista": ["vermelho", "verde", "azul"],
    "pontos_tupla": (5, 10, 15),
    "nomes_lista": ["Alice", "Bob", "Carol"],
    "coordenadas_tupla": ((1, 2), (3, 4), (5, 6))
}

print(meu_dicionario.values())
lista = list(meu_dicionario.values())
for x in lista:
    for y in x:

        if type(y) == tuple:
            for z in y:
                print(z)
        else:
            print(y)