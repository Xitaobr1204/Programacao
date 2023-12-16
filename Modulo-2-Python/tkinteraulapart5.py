from tkinter import *

janela = Tk()

text = Text(janela, height=5, width=45)
text.pack()

text.insert(END, 'SOLICITE AO GPT: ')

botao = Button(janela,text='enviar')
botao.pack()

janela.mainloop()