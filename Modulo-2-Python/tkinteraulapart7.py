from tkinter import *
from tkinter import ttk

janela = Tk()

canvas = Canvas(janela, width=300,height=150)
canvas.pack()

canvas.create_oval(75,150,30,10)
canvas.create_rectangle(10,10,20,40, fill='blue')

botao = Button (canvas, text='testando')
botao.pack()

janela.mainloop()