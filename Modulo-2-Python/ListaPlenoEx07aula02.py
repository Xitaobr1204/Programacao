#7)Você recebeu uma lista de tuplas, onde cada tupla contém o nome de um produto e seu
#preço. Por exemplo: [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]. Escreva um programa
#que itere sobre essa lista e calcule o valor total dos produtos, exibindo-os na tela.
#ex: “Maça = R$2,50”
lista_de_produtos = [("Maçã", 2.50), ("Banana", 1.75), ("Laranja", 3.00)]

valor_total = 0

for produto, preco in lista_de_produtos:
    print(f"{produto} = R${preco:.2f}")

    valor_total += preco

print(f"Valor total dos produtos: R${valor_total:.2f}")
