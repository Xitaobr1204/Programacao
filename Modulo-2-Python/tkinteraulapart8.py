import tkinter as tk
root = tk.Tk()

checkvar = tk.BooleanVar()

checkbutton = tk.Checkbutton(root,text='Aceitar Termos',variable=checkvar)
checkbutton.pack()

root.mainloop()