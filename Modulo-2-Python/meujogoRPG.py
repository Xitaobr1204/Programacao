import random

class Jogador:
    def __init__(self, nome, classe, vida, ataque, defesa):
        self.nome = nome
        self.classe = classe
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, inimigo):
        dano_causado = max(0, self.ataque - inimigo.defesa)
        inimigo.vida -= dano_causado
        return dano_causado

class Inimigo:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, jogador):
        dano_causado = max(0, self.ataque - jogador.defesa)
        jogador.vida -= dano_causado
        return dano_causado

def criar_conta():
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    return {"nome": nome, "senha": senha, "personagem": None}

def fazer_login(contas):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    if nome in contas and contas[nome]["senha"] == senha:
        print(f"Bem-vindo de volta, {nome}!")
        return contas[nome]["personagem"]
    else:
        print("Nome de usuário ou senha incorretos.")
        return None

def criar_personagem():
    nome_personagem = input("Digite o nome do seu personagem: ")
    return Jogador(nome_personagem, "Guerreiro", 100, 20, 10)

def batalha(jogador, inimigo):
    print(f"Batalha iniciada: {jogador.nome} vs {inimigo.nome}")
    
    while jogador.vida > 0 and inimigo.vida > 0:
        print(f"\n{jogador.nome}: Vida = {jogador.vida}, {inimigo.nome}: Vida = {inimigo.vida}")
        
        # Vez do jogador
        input("Pressione Enter para atacar...")
        dano_jogador = jogador.atacar(inimigo)
        print(f"{jogador.nome} causou {dano_jogador} de dano a {inimigo.nome}")

        # Verifica se o inimigo foi derrotado
        if inimigo.vida <= 0:
            print(f"\n{jogador.nome} venceu a batalha!")
            break

        # Vez do inimigo
        dano_inimigo = inimigo.atacar(jogador)
        print(f"{inimigo.nome} causou {dano_inimigo} de dano a {jogador.nome}")

        # Verifica se o jogador foi derrotado
        if jogador.vida <= 0:
            print(f"\n{jogador.nome} foi derrotado. {inimigo.nome} venceu a batalha.")
            break

# Sistema principal
contas = {}

while True:
    print("\n1. Criar Conta")
    print("2. Fazer Login")
    print("3. Sair")
    
    escolha = input("Escolha a opção: ")

    if escolha == "1":
        nova_conta = criar_conta()
        contas[nova_conta["nome"]] = {"senha": nova_conta["senha"], "personagem": None}
        print("Conta criada com sucesso!")

    elif escolha == "2":
        personagem_atual = fazer_login(contas)
        if personagem_atual is not None:
            if personagem_atual is None:
                novo_personagem = criar_personagem()
                contas[personagem_atual["nome"]]["personagem"] = novo_personagem
                personagem_atual = novo_personagem

            inimigo = Inimigo("Monstro", 50, 15, 5)
            batalha(personagem_atual, inimigo)

    elif escolha == "3":
        break

    else:
        print("Opção inválida. Tente novamente.")
