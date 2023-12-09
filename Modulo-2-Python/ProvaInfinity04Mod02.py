def calcular_media(notas):
    return sum(notas) / len(notas) if len(notas) > 0 else 0

def verificar_situacao(media):
    if media == 10:
        return "Parabéns, sua média é 10!"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Digita notas
try:
    quantidade_notas = int(input("Quantas notas você deseja digitar? "))
except ValueError:
    print("Por favor, digite um número válido.")
    quit()

notas = []

# Pede as notas
for i in range(quantidade_notas):
    try:
        nota = float(input(f"Digite a nota {i + 1}: "))
    except ValueError:
        print("Por favor, digite uma nota válida.")
        quit()
    notas.append(nota)

# Média 
media_aluno = calcular_media(notas)
situacao_aluno = verificar_situacao(media_aluno)

# Resultado
print(f"A média do aluno é: {media_aluno}")
print(f"Situação do aluno: {situacao_aluno}")