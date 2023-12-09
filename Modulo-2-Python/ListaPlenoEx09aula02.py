#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.	

idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))

    idades.append(idade)
    alturas.append(altura)


print("\nIdades e alturas na ordem inversa:")
for i in range(4, -1, -1):
    print(f"Idade: {idades[i]}, Altura: {alturas[i]} metros")