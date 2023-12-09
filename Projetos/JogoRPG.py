import pickle
import os

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.personagem = None

class Personagem:
    def __init__(self, forca, inteligencia, cor_pele, cabelo):
        self.forca = forca
        self.inteligencia = inteligencia
        self.cor_pele = cor_pele
        self.cabelo = cabelo

def cadastrar_usuario(username, password):
    novo_usuario = Usuario(username, password)
    return novo_usuario

def criar_personagem(forca, inteligencia, cor_pele, cabelo):
    novo_personagem = Personagem(forca, inteligencia, cor_pele, cabelo)
    return novo_personagem

def salvar_usuario(usuario):
    with open(f"{usuario.username}.dat", "wb") as file:
        pickle.dump(usuario, file)

def carregar_usuario(username):
    try:
        with open(f"{username}.dat", "rb") as file:
            return pickle.load(file)
    except:
        return None

def menu_principal():
    print("1. Criar Conta")
    print("2. Fazer Login")
    print("3. Sair")

def menu_usuario(usuario):
    print("1. Personalizar Personagem")
    print("2. Visualizar Personagem")
    print("3. Logout")

def main():
    while True:
        menu_principal()
        escolha = input("Escolha a opção (1/2/3): ")

        if escolha == "1":
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")

            novo_usuario = cadastrar_usuario(username, password)
            salvar_usuario(novo_usuario)
            print("Conta criada com sucesso!")

        elif escolha == "2":
            username = input("Digite o nome de usuário: ")
            password = input("Digite a senha: ")

            usuario = carregar_usuario(username)

            if usuario and usuario.password == password:
                while True:
                    menu_usuario(usuario)
                    escolha_usuario = input("Escolha a opção (1/2/3): ")

                    if escolha_usuario == "1":
                        forca = int(input("Força (1-10): "))
                        inteligencia = int(input("Inteligência (1-10): "))
                        cor_pele = input("Cor da pele: ")
                        cabelo = input("Tipo de cabelo: ")

                        usuario.personagem = criar_personagem(forca, inteligencia, cor_pele, cabelo)
                        salvar_usuario(usuario)
                        print("Personagem personalizado com sucesso!")

                    elif escolha_usuario == "2":
                        if usuario.personagem:
                            print(f"Personagem de {usuario.username}:")
                            print(f"Força: {usuario.personagem.forca}")
                            print(f"Inteligência: {usuario.personagem.inteligencia}")
                            print(f"Cor da pele: {usuario.personagem.cor_pele}")
                            print(f"Tipo de cabelo: {usuario.personagem.cabelo}")
                        else:
                            print("Você ainda não personalizou seu personagem.")

                    elif escolha_usuario == "3":
                        print("Logout realizado com sucesso!")
                        break

                    else:
                        print("Opção inválida. Tente novamente.")

            else:
                print("Usuário ou senha incorretos. Tente novamente.")

        elif escolha == "3":
            print("Saindo do jogo. Até a próxima!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
