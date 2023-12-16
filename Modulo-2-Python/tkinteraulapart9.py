import tkinter as tk

root = tk.Tk()

radiovar = tk.StringVar()

radio1 = tk.Radiobutton(root, text='Opção 1', variable=radiovar, value='Opção 1')
radio2 = tk.Radiobutton(root, text='Opção 2', variable=radiovar, value='Opção 2')
radio1.pack()
radio2.pack()

root.mainloop()