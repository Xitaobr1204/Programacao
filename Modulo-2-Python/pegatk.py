import tkinter as tk
from tkinter import messagebox

def verificar_login():
    # Obter os valores dos campos de entrada
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    # Verificar se o login é válido (substitua isso com sua lógica de validação real)
    if usuario == "usuario" and senha == "senha":
        messagebox.showinfo("Login bem-sucedido", "Bem-vindo, {}!".format(usuario))
    else:
        messagebox.showerror("Login falhou", "Usuário ou senha incorretos.")

# Criar a janela principal
root = tk.Tk()
root.title("Login")

# Criar os rótulos e campos de entrada
label_usuario = tk.Label(root, text="Usuário:")
label_senha = tk.Label(root, text="Senha:")
entry_usuario = tk.Entry(root)
entry_senha = tk.Entry(root, show="*")  # A opção show="*" mascara a senha com asteriscos

# Criar o botão de login
botao_login = tk.Button(root, text="Login", command=verificar_login)

# Posicionar os widgets usando grid
label_usuario.grid(row=0, column=0, sticky=tk.E)
label_senha.grid(row=1, column=0, sticky=tk.E)
entry_usuario.grid(row=0, column=1)
entry_senha.grid(row=1, column=1)
botao_login.grid(row=2, column=1, pady=10)

# Iniciar o loop principal
root.mainloop()