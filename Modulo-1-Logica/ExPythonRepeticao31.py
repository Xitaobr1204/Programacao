#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

#Lojas Tabajara 
#Produto 1: R$ 2.20
#Produto 2: R$ 5.80
#Produto 3: R$ 0
#Total: R$ 9.00
#Dinheiro: R$ 20.00
#Troco: R$ 11.00

from os import system

controle1 = True
cliente = 1

while controle1 == True: #caixa registradora rodar
    print(f'Cliente nº {cliente}', end=' ')
    print()

    controle2 = True
    nump = 1
    total = 0

#Condição de repetição
    while controle2 == True:
        valor = input(f'Produto {nump}: ')
        preco = float(valor)

    #Condição de parada do while(controle)
        if preco == 0.0:
            controle2 = False

        nump = nump + 1

        total = total + preco
        
    else:
            print(f'Total da compra: R$ {total}')
            valor = input('Pagamento (R$) em dinheiro: ')
            valor = float(valor)
            print(f'Troco (R$): {valor - total}')
            cliente = cliente + 1
            input('Aperte o ENTER para o próximo cliente...')
            system('cls')