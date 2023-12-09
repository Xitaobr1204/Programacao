def registro(**kwargs):
    return kwargs.get

nome = input('Informe o nome: ')
idade = input('Informe a idade: ')
sangue = input('Informe o tipo sanguíneo: ')
f = registro(Nome = nome, Idade = idade, Tipo = sangue)
print(f)