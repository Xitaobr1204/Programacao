from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
janela = Tk()
janela.title('Exemplo Arvore')

arvore = Treeview(janela)

#DEFINE AS COLUNAS
arvore["columns"] = ("nome","email","telefone")

#POSICIONA AS COLUNAS
arvore.column("#0", width=100 ,minwidth=150 , anchor= CENTER)
arvore.column("nome", width=150 ,minwidth=150 , anchor= CENTER)
arvore.column("email", width=150 ,minwidth= 150, anchor= CENTER)
arvore.column("telefone", width=150 ,minwidth=150 , anchor= CENTER)

#NOMES NAS COLUNAS
arvore.heading("#0", text="ID")
arvore.heading("nome", text="NOME")
arvore.heading("email", text="EMAIL")
arvore.heading("telefone", text="TEL")
arvore.pack()

#INSERINDO DADOS NA ARVORE
for x in range(10):
    arvore.insert("", END, text=f'{x}', values=('Otavio', 'otavio@gmail.com', '319872432'))


janela.mainloop()