lista_de_produtos = []
total_produtos = 0.0

def adicionar_produto():
    global total_produtos
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    valor_unitario = float(input("Digite o valor unitário do produto: "))

    total_produto = quantidade * valor_unitario

    total_produtos += total_produto

    produto = {
        "produto": nome,
        "quantidade": quantidade,
        "valor": valor_unitario,
        "total": total_produto
    }
    lista_de_produtos.append(produto)

    print(f"Produto {nome} adicionado com sucesso!\n")

def ver_lista():
    print("Lista de produtos:")
    for produto in lista_de_produtos:
        print(f"Produto: {produto['produto']}, Quantidade: {produto['quantidade']}, Valor Unitário: {produto['valor']}, Total: {produto['total']}")
    print(f"Valor Total de Todos os Produtos: {total_produtos}\n")

def atualizar_produto():
    global total_produtos
    nome = input("Digite o nome do produto que deseja atualizar: ")

    for produto in lista_de_produtos:
        if produto["produto"] == nome:
            nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            novo_valor_unitario = float(input("Digite o novo valor unitário do produto: "))
            
            produto["quantidade"] = nova_quantidade
            produto["valor"] = novo_valor_unitario
            produto["total"] = nova_quantidade * novo_valor_unitario
            total_produtos = sum(p["total"] for p in lista_de_produtos)

            print(f"Informações do produto {nome} atualizadas com sucesso!\n")
            return

    print(f"Produto {nome} não encontrado.\n")

def remover_produto():
    global total_produtos
    nome = input("Digite o nome do produto que deseja remover: ")

    for produto in lista_de_produtos:
        if produto["produto"] == nome:
            total_produtos -= produto["total"]
            
            lista_de_produtos.remove(produto)

            print(f"Produto {nome} removido com sucesso!\n")
            return

    print(f"Produto {nome} não encontrado.\n")

while True:
    print("1. Adicionar Produto")
    print("2. Ver Lista de Produtos")
    print("3. Atualizar Produto")
    print("4. Remover Produto")
    print("5. Encerrar Programa")

    escolha = input("Escolha uma opção (1-5): ")

    if escolha == "1":
        adicionar_produto()
    elif escolha == "2":
        ver_lista()
    elif escolha == "3":
        atualizar_produto()
    elif escolha == "4":
        remover_produto()
    elif escolha == "5":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
