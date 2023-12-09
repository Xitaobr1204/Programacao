#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite o seu nome:')
idade = input('Digite a sua idade:')
salario = input('Digite o seu salário:')
sexo = input('Sexo: F-feminino / M-Masculino:')
estadoc = input('Estado civil: S-Solteiro/C-Casado/V-Viúvo/D-Divorciado')

while True:
    nome = input('Digite o seu nome(maior que 3 caracteres):')
    if len(nome) > 3:
        break
    else:
        print('Nome deve ter mais que 3 caracteres.')

while True:
    idade = int(input('Digite sua idade(entre 0 e 150):'))
    if 0 <= idade <= 150:
        break
    else:
        print('Idade deve estar entre 0 e 150.')

while True:
    salario = float(input('Digite o seu salário(maior que zero):'))
    if salario > 0:
        break
    else:
        print('Salário deve ser maior que zero')

while True:
    sexo = input('Digite o seu sexo(f-feminino/m-masculino):').lower()
    if sexo in ['f','m']:
        break
    else:
        print('Sexo deve ser f ou m.')

while True:
    estadoc = input('Estado civil: c para casado, s para solteiro, d para divorciado, v para viúvo:').lower()  
    if estadoc in ['c','s','d','v']:
        break
    else:
        print('Estado civil deve ser s,c,d ou v')

        print('Todas as informações são válidas.')