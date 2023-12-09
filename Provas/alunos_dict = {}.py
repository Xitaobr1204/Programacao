alunos_dict = {}

def AdicionarAluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite o número de matrícula do aluno: ")


    alunos_dict[matricula] = nome
    print(f"Aluno {nome} adicionado com sucesso!\n")

def RemoverAluno():
    matricula = input("Digite o número de matrícula do aluno a ser removido: ")


    if matricula in alunos_dict:
        nome = alunos_dict.pop(matricula)
        print(f"Aluno {nome} removido com sucesso!\n")
    else:
        print("Matrícula não encontrada.\n")


def AtualizarAluno():
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ")

    if matricula in alunos_dict:
        nome = input("Digite o novo nome do aluno: ")
        alunos_dict[matricula] = nome
        print(f"Nome do aluno atualizado com sucesso!\n")
    else:
        print("Matrícula não encontrada.\n")


def VerAlunos():
    if not alunos_dict:
        print("Nenhum aluno cadastrado.\n")
    else:
        print("Lista de alunos:")
        for matricula, nome in alunos_dict.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")
        print()


if __name__ == "__main__":
    while True:
        print("1. Adicionar Aluno")
        print("2. Remover Aluno")
        print("3. Atualizar Aluno")
        print("4. Ver Alunos")
        print("5. Sair")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "1":
            AdicionarAluno()
        elif escolha == "2":
            RemoverAluno()
        elif escolha == "3":
            AtualizarAluno()
        elif escolha == "4":
            VerAlunos()
        elif escolha == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

