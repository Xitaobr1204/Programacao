from tkinter import * 
def clicou():
    print('Foi clicado')

janela = Tk()

text = Label(janela, text='')
botao = Button(janela, text = 'clicar',command=clicou)
botao.pack()

janela.mainloop()