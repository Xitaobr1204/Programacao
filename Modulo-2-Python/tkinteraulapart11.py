import tkinter as tk 

root = tk.Tk()

menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='Arquivo', menu=filemenu)
filemenu.add_command(label='Abrir')
filemenu.add_command(label='Salvar')
filemenu.add_separator()
filemenu.add_command(label='Sair')

root.mainloop()