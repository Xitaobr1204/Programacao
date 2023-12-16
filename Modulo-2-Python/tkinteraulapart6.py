from tkinter import *

janela = Tk()

quadro = Frame(janela, relief=RAISED,borderwidth=2)
quadro.pack()

texto = Label(quadro, text='12121213332211')
texto.pack()

texto2 = Label(janela, text='12121213332211')
texto2.pack()

janela.mainloop()