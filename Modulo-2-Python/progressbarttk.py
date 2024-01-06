from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
janela = Tk()
janela.title('Exemplo combobox')

barra = Progressbar(janela, orient='horizontal', length=200, mode='determinate')
barra.pack()
barra.start(10)

janela.mainloop()
