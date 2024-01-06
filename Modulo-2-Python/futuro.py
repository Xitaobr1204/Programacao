from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title('pesadão')

label = Label(janela, text='carregando...')
label.pack()

barra = Progressbar(janela, orient='horizontal', length=200, mode='determinate')
barra.pack()
barra.start(50)

janela.mainloop()