#Faça um Programa que leia 4 notas, mostre as notas e a média na tela. utilizar listas
notas = []

for i in range(4):
    nota = float(input(f'Digite a nota {i + 1}:'))
    notas.append(nota)

#Exibir as notas digitadas
print('Notas digitadas')
for i, nota in enumerate(notas, start=1):
    print(f'Nota {i}: {nota}')

#Média
media = sum(notas) / len(notas)

#Exibir a média
print(f'A média das notas é: ',media)