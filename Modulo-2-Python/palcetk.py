#focar na explicação de posicionamento
#pack()
from tkinter import *
janela = Tk()

label = Label(janela, text='PLACE 1')
label.place(x=0, y=0)

label2 = Label(janela, text='PLACE 2')
label2.place(x=50, y=0)

#O padx e pady vai esta referenciado ao espaçamento interno

label3 = Label(janela, text='PLACE 3')
label3.place(x=100, y=0)



janela.mainloop()