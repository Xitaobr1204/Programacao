import tkinter as tk
from time import strftime

def atualizar_hora():
    hora_atual = strftime('%H:%M:%S %p')  # Formato de 12 horas com AM/PM
    label_hora.config(text=hora_atual)
    label_hora.after(1000, atualizar_hora)  # Agendar a próxima atualização após 1000ms (1 segundo)

# Configuração da janela principal
root = tk.Tk()
root.title("Relógio Digital")

# Rótulo para exibir a hora
label_hora = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label_hora.pack(anchor='center')

# Iniciar a função para atualizar a hora
atualizar_hora()

# Iniciar o loop principal da interface gráfica
root.mainloop()