import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_322=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_322["font"] = ft
        GLabel_322["fg"] = "#333333"
        GLabel_322["justify"] = "center"
        GLabel_322["text"] = "login"
        GLabel_322.place(x=70,y=80,width=72,height=32)

        GLineEdit_680=tk.Entry(root)
        GLineEdit_680["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_680["font"] = ft
        GLineEdit_680["fg"] = "#333333"
        GLineEdit_680["justify"] = "center"
        GLineEdit_680["text"] = ""
        GLineEdit_680.place(x=140,y=80,width=126,height=30)

        GLabel_432=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_432["font"] = ft
        GLabel_432["fg"] = "#333333"
        GLabel_432["justify"] = "center"
        GLabel_432["text"] = "senha"
        GLabel_432.place(x=70,y=120,width=70,height=25)

        GLineEdit_296=tk.Entry(root)
        GLineEdit_296["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_296["font"] = ft
        GLineEdit_296["fg"] = "#333333"
        GLineEdit_296["justify"] = "center"
        GLineEdit_296["text"] = ""
        GLineEdit_296.place(x=140,y=120,width=126,height=30)

        GButton_812=tk.Button(root)
        GButton_812["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_812["font"] = ft
        GButton_812["fg"] = "#000000"
        GButton_812["justify"] = "center"
        GButton_812["text"] = "Enter"
        GButton_812.place(x=170,y=160,width=70,height=25)
        GButton_812["command"] = self.GButton_812_command

    def GButton_812_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
