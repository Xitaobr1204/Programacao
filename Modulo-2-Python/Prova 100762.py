#[PY-A03] Crie um programa em Python que permita adicionar, remover e visualizar alunos e seus números de matrícula usando um dicionário.
#O programa deve fornecer as seguintes funcionalidades:
#Adicionar um aluno: O usuário poderá adicionar o nome e o número de matrícula de um aluno ao dicionário.
#Remover um aluno: O usuário poderá remover um aluno do dicionário informando o número de matrícula.
#Visualizar todos os alunos: O usuário poderá visualizar todos os alunos registrados no dicionário, exibindo seus respectivos números de matrícula.
#O programa deve ser executado em um loop contínuo até que o usuário escolha sair.
alunos = {}

def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite o número de matrícula do aluno: ')
    alunos[matricula] = nome
    print(f'Aluno {nome} com matrícula {matricula} adicionado.')

def remover_aluno():
    matricula = input('Digite o número de matrícula do aluno a ser removido: ')
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print(f'Aluno {nome} com matrícula {matricula} removido.')
    else:
        print('Matrícula não encontrada.')

def visualizar_alunos():
    print('Lista de alunos:')
    if alunos:
        for matricula, nome in alunos.items():
            print(f'Matrícula: {matricula}, Nome: {nome}')
    else:
        print('Nenhum aluno registrado.')

while True:
    print('\nEscolha uma opção:')
    print('1. Adicionar aluno')
    print('2. Remover aluno')
    print('3. Visualizar todos os alunos')
    print('4. Sair')

    escolha = input('Digite o número da opção desejada: ')

    if escolha == '1':
        adicionar_aluno()
    elif escolha == '2':
        remover_aluno()
    elif escolha == '3':
        visualizar_alunos()
    elif escolha == '4':
        print('Encerrado!!!!!')
        break
    else:
        print('Opção inválida. Escolha novamente.')
    