from tkinter import *

janela = Tk()

tipodado = StringVar()
enter = Entry(janela, textvariable= tipodado)
enter.pack()

janela.mainloop()