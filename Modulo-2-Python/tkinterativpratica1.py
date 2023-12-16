import tkinter as tk

def cadastrar_aluno():
    nome = entry_nome.get()
    idade = entry_idade.get()
    nota = entry_nota.get()

    # Exibir os dados no terminal
    print("Aluno cadastrado:")
    print("Nome:", nome)
    print("Idade:", idade)
    print("Nota:", nota)
    print("----------------------")

    # Limpar as entradas após o cadastro
    entry_nome.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_nota.delete(0, tk.END)

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Alunos")

# Rótulos e entradas para nome, idade e nota
label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

label_idade = tk.Label(root, text="Idade:")
label_idade.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_nota = tk.Entry(root)
entry_nota.grid(row=2, column=1, padx=10, pady=10)

# Botão para cadastrar aluno
btn_cadastrar = tk.Button(root, text="Cadastrar Aluno", command=cadastrar_aluno)
btn_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
