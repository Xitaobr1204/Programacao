#Menu calculadora
var = True
while var == True:
    print('### MENU ###')
    print('Digite a tarefa que deseja executar: ')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Encerrar')
    escolha = int(input('Escolha o tipo de operação: '))
#Soma
    if escolha == 1:
        var1=int(input('Digite o primeiro número para realizar o que deseja: '))
        var2=int(input('Digite o primeiro número para realizar o que deseja: '))
        print('Soma: ',soma(var1 , var2))
#Subtração
    if escolha == 2:
        var1=int(input('Digite o primeiro número para realizar o que deseja: '))
        var2=int(input('Digite o primeiro número para realizar o que deseja: '))
        print('Resultado: ',subtracao(var1 , var2))
#Multiplicação
    if escolha == 3:
        var1=int(input('Digite o primeiro número para realizar o que deseja: '))
        var2=int(input('Digite o primeiro número para realizar o que deseja: '))
        print('Resultado: ',multiplicacao(var1 , var2))
#Divisão
    if escolha == 4:
        var1=int(input('Digite o primeiro número para realizar o que deseja: '))
        var2=int(input('Digite o primeiro número para realizar o que deseja: '))
        print('Resultado: ',divisao(var1 , var2))
#Sair
    if escolha == 5:
        var = False
        print('Operação encerrada com sucesso, até breve!!!!')