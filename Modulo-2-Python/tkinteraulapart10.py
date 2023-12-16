import tkinter as tk

root = tk.Tk()

scalevar = tk.DoubleVar()
scale = tk.Scale(root,from_=8, to=100,orient=tk.HORIZONTAL,variable=scalevar)
scale.pack()

root.mainloop()