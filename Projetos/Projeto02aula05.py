#Crie um sistema de cadastro de pessoas onde
#você deve ter a opção de cadastrar nome, idade e nível
#salvar em um dicionário estes valores e incluir a uma
#grande lista para pode consultar utilizando o nome da pessoa
#deve ter também uma função para aumentar o nível do
#cadastrado e uma função para deletar determinado
#cadastro de usuário.

cadastros = []

def cadastrar_pessoa():
    nome = input('Digite o nome da pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))
    nivel = int(input('Digite o nível da pessoa: '))


    pessoa = {'nome': nome, 'idade': idade, 'nivel': nivel}

    cadastros.append(pessoa)
    print(f'{nome} foi cadastrado com sucesso!')

def aumentar_nivel():
    nome = input('Digite o nome da pessoa que terá o nível aumentado: ')
    for pessoa in cadastros:
        if pessoa['nome'] == nome:
            pessoa['nivel'] += 1
            print(f'O nível de {nome} foi aumentado para {pessoa["nivel"]}.')
            return
    print(f'{nome} não foi encontrado nos cadastros.')

def deletar_cadastro():
    nome = input('Digite o nome da pessoa que deseja excluir: ')
    for pessoa in cadastros:
        if pessoa['nome'] == nome:
            cadastros.remove(pessoa)
            print(f'{nome} foi removido dos cadastros.')
            return
    print(f'{nome} não foi encontrado nos cadastros.')

def consultar_cadastro():
    nome = input('Digite o nome da pessoa que deseja consultar: ')
    for pessoa in cadastros:
        if pessoa['nome'] == nome:
            print(f'Nome: {pessoa["nome"]}, Idade: {pessoa["idade"]}, Nível: {pessoa["nivel"]}')
            return
    print(f'{nome} não foi encontrado nos cadastros.')

while True:
    print('\n=== Menu ===')
    print('1. Cadastrar Pessoa')
    print('2. Aumentar Nível')
    print('3. Deletar Cadastro')
    print('4. Consultar Cadastro')
    print('0. Sair')

    escolha = input('Escolha uma opção (0-4): ')

    if escolha == '1':
        cadastrar_pessoa()
    elif escolha == '2':
        aumentar_nivel()
    elif escolha == '3':
        deletar_cadastro()
    elif escolha == '4':
        consultar_cadastro()
    elif escolha == '0':
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente novamente.')
