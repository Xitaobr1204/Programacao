import tkinter as tk
from tkinter import ttk

def adicionar_item():
    # Obtém o item selecionado na Entry e adiciona ao Treeview
    item_text = entry.get()
    tree.insert('', 'end', text=item_text)

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo Treeview")

# Criar um Treeview
tree = ttk.Treeview(root)
tree["columns"] = ("column1", "column2")  # Define as colunas

# Configurar as colunas
tree.column("#0", width=150, minwidth=150, stretch=tk.NO)  # Coluna especial para os textos principais
tree.column("column1", width=100, minwidth=100, anchor=tk.W)
tree.column("column2", width=100, minwidth=100, anchor=tk.W)

# Adicionar cabeçalhos de coluna
tree.heading("#0", text="Item")
tree.heading("column1", text="Coluna 1")
tree.heading("column2", text="Coluna 2")

# Adicionar alguns itens de exemplo
tree.insert('', 'end', text="Item A", values=("Valor 1A", "Valor 2A"))
tree.insert('', 'end', text="Item B", values=("Valor 1B", "Valor 2B"))
tree.insert('', 'end', text="Item C", values=("Valor 1C", "Valor 2C"))

# Adicionar uma Entry para inserir novos itens
entry = tk.Entry(root)
entry_button = tk.Button(root, text="Adicionar Item", command=adicionar_item)

# Posicionar widgets usando pack ou grid
entry.pack(pady=10)
entry_button.pack(pady=5)
tree.pack(expand=True, fill="both")

# Iniciar o loop principal
root.mainloop()