from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
janela = Tk()
janela.title('Exemplo combobox')

dias_da_semana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

combobox = Combobox(janela, values= dias_da_semana)
combobox.pack(padx=75, pady=20)

janela.mainloop()