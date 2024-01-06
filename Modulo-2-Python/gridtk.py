#focar na explicação de posicionamento
#pack()
from tkinter import *
janela = Tk()

label = Label(janela, text='GRID 1')
label.grid(row=1, column=3, padx=10, pady=20)

label2 = Label(janela, text='GRID 2')
label2.grid(row=2, column=3, padx=0, pady=0)
#O padx e pady vai esta referenciado ao espaçamento interno

label2 = Label(janela, text='GRID 3')






janela.mainloop()