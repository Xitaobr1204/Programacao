#focar na explicação de posicionamento
#pack()
from tkinter import *
janela = Tk()

label = Label(janela, text='Relembrando a tkinter 1')
label.pack( padx=10, pady=5)

label2 = Label(janela, text='Relembrando a tkinter 2')
label2.pack(padx=0, pady=20)

label2 = Label(janela, text='Relembrando a tkinter 3')
label2.pack( padx=10, pady=100)

'''
Parâmetros comuns:
side: Especifica em qual lado do contêiner principal o widget deve ser empacotado. Pode ser 'top', 'bottom', 'left' ou 'right'.
fill: Define como o widget deve se expandir para preencher o espaço alocado. Pode ser 'none' (nenhum), 'x' (horizontal), 'y' (vertical) ou 'both' (ambos).
expand: Aceita um valor booleano que determina se o widget deve se expandir para preencher qualquer espaço adicional no contêiner.
anchor: Controla a posição do widget dentro do espaço alocado. Pode ser 'n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', ou 'center'.
padx e pady: Adiciona espaço de preenchimento horizontal (padx) ou vertical (pady) ao redor do widget.
'''



janela.mainloop()