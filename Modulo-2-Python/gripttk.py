from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
janela = Tk()
janela.title('Exemplo combobox')
janela.resizable(True, True)

label = Label(janela, text='GRIP')
label.pack()

size = Sizegrip(janela)
size.pack(anchor=SE, padx=3, pady=3, expand=True)


janela.mainloop()