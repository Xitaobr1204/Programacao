#Crie um programa que solicite ao usuario o tamanho da lista que deseja e peça para informar os dados e insira cada um na lista
def criar_lista():  
    tamanho_lista = int(input('Insira o tamanho da lista que você deseja: '))
    minhalista = []
    for x in range (tamanho_lista):
        dadouser = input('Insira um dado que deseja adicionar a lista: ')
        minhalista.append(dadouser)
        
    return minhalista
lista_criada = criar_lista()
print(f'Lista criada', lista_criada)