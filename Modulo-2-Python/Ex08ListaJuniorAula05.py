#utilizando lambda faça uma função de divisao e lembrando que n pode ser dividido por 0
x = lambda a,b: a / b
pergunta1 = int(input('Insira um número: '))
pergunta2 = int(input('Insira o segundo número: '))
if pergunta1 or pergunta2 == 0:
    print('Função não disponível, o número não pode ser dividido por zero!!!')
else:
    print('Resultado da divisão solicitada: ',pergunta1/pergunta2)