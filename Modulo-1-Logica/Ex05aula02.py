#Entrada de dados
aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite o valor da primeira nota:'))
n2 = float(input('Digite o valor da segunda nota:'))
n3 = float(input('Digite o valor da terceira nota:'))
#Média
media=(n1+n2+n3)/3

#Calcular a média
print(F'O aluno {aluno} teve média de {media}.')

#Códigos para responder ao aluno
if (media >= 6):
    print('APROVADO.PARABENS!')
elif media >= 4 and media < 6:
    print('REPROVADO.')
else:
    print('REPROVADO.')