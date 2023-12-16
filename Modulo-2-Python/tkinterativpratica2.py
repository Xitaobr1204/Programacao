import tkinter as tk

def press_button(value):
    current_expression = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_expression + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        print("Resultado:", result)
        clear_entry()
    except Exception as e:
        print("Erro ao calcular:", e)
        clear_entry()

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Entrada para exibir a expressão
entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Botões numéricos
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2,
              command=lambda button=button: press_button(button) if button != '=' else calculate()).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Iniciar o loop principal da interface gráfica
root.mainloop()
