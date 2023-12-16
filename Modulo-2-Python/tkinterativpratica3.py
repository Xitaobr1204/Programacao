import tkinter as tk

def converter_temperatura():
    try:
        temperatura_origem = float(entry_temperatura.get())
        unidade_origem = combo_origem.get()
        unidade_destino = combo_destino.get()

        if unidade_origem == unidade_destino:
            print("As unidades de origem e destino são iguais. Nenhuma conversão necessária.")
            return

        if unidade_origem == "Celsius" and unidade_destino == "Fahrenheit":
            resultado = (temperatura_origem * 9/5) + 32
        elif unidade_origem == "Fahrenheit" and unidade_destino == "Celsius":
            resultado = (temperatura_origem - 32) * 5/9
        else:
            print("Conversão não suportada.")
            return

        print(f"{temperatura_origem} {unidade_origem} é igual a {resultado:.2f} {unidade_destino}")

    except ValueError:
        print("Por favor, insira uma temperatura válida.")

# Configuração da janela principal
root = tk.Tk()
root.title("Conversor de Temperatura")

# Rótulo e entrada para a temperatura
label_temperatura = tk.Label(root, text="Temperatura:")
label_temperatura.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_temperatura = tk.Entry(root)
entry_temperatura.grid(row=0, column=1, padx=10, pady=10)

# Menu suspenso para escolher a unidade de origem
label_origem = tk.Label(root, text="De:")
label_origem.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
unidades = ["Celsius", "Fahrenheit"]
combo_origem = tk.StringVar(root)
combo_origem.set(unidades[0])  # Definir o valor padrão
menu_origem = tk.OptionMenu(root, combo_origem, *unidades)
menu_origem.grid(row=1, column=1, padx=10, pady=10)

# Menu suspenso para escolher a unidade de destino
label_destino = tk.Label(root, text="Para:")
label_destino.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
combo_destino = tk.StringVar(root)
combo_destino.set(unidades[1])  # Definir o valor padrão
menu_destino = tk.OptionMenu(root, combo_destino, *unidades)
menu_destino.grid(row=2, column=1, padx=10, pady=10)

# Botão para realizar a conversão
btn_converter = tk.Button(root, text="Converter", command=converter_temperatura)
btn_converter.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
