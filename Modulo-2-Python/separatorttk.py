from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
janela = Tk()
janela.title('Exemplo combobox')

barra1 = Progressbar(janela, orient='horizontal', length=200, mode='determinate')
barra1.pack()
barra1.start(10)

separar = Separator(janela, orient=HORIZONTAL)
separar.pack(padx=50, pady=10)

label = Label(janela, text='separando . . .')
label.pack()
janela.mainloop()