#Crie uma calculadora com um menu
#interativo, onde deve efetuar as
#operações básicas (+
#,-,/,
#*) obedecendo as
#regras matemáticas.
#obs: O grau de complexidade da
#calculadora vai do seu conhecimento,
#se quiser fazer básica ou com todas as
#características de um bom código
#PARTE 1''''''''''''''''''
#Adição
def soma (a,b):
    return a+b
#Subtração
def subtracao (a,b):
    return a-b
#Multiplicação
def multiplicacao (a,b):
    return a*b
#Divisão
def divisao (a,b):
    if b == 0:
        print('Erro.Divisão por zero')
    
    else:
        return a/b   

#PARTE 2'''''''''''''''''
while True:
    print('\nMenu.')
    print('1.Adição')
    print('2.Subtração')
    print('3.Multiplicação')
    print('4.Divisão')
    print('5.Sair')

    escolha = input('Selecione qual será a sua escolha: ')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    if escolha == '1':
        print(soma(n1,n2))
    if escolha == '2':
        print(subtracao(n1,n2))
    if escolha == '3':
        print(multiplicacao(n1,n2))
    if escolha == '4':
        print(divisao(n1,n2))
    if escolha == '5':
        print('Programa encerrado!!!!!!')
else:
    print('Erro!!!!!')        