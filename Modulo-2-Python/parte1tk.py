#iniciamos fazendo a importação do framework
from tkinter import *
#instanciamos o objeto que iremos trabalhar a partir deste ponto conseguimos utilizar todos os metodos disponiveis 
#no framework
janela = Tk()

#criamos tudo que precisamos
#label (Rotulo)
label = Label(janela, text='Relembrando a tkinter')
label.pack()

#Button (botao)
def botao_clicado():
    label.config(text='Botao clicado')
    
botao = Button(janela, text='Clique aqui!!', command=botao_clicado)
botao.pack()

#colocamos o programa para rodar em um loop

janela.mainloop()