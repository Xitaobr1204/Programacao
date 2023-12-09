#Com o dicionário da questão 1, mostre ao usuário a lista de chaves e pergunte se ele quer eliminar algum item. Caso a resposta seja 'SIM', solicite o item que deseja deletar e elimine-o do dicionário.
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
print("Itens disponíveis no sacolão:")
for item in sacolao:
    print(item)

eliminar = input("Deseja eliminar algum item? (SIM ou NÃO): ").upper()

if eliminar == "SIM":
    item_a_deletar = input("Digite o nome do item que deseja deletar: ")

if item_a_deletar in sacolao:
        del sacolao[item_a_deletar]
        print(f"O item '{item_a_deletar}' foi removido do sacolão.")
else:
        print("Item não encontrado no sacolão.")
else:
print("Nenhum item foi removido. O sacolão permanece inalterado.")

print("Dicionário atualizado:", sacolao)
