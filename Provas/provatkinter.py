import tkinter as tk

def converter_cm_para_m():
    try:
        # Obter o valor em centímetros
        cm_valor = float(entry_cm.get())

        # Converter para metros
        m_valor = cm_valor / 100

        # Atualizar o rótulo com o resultado
        resultado_var.set(f'{cm_valor} cm é igual a {m_valor} metros')
    except ValueError:
        resultado_var.set('Digite um valor válido em centímetros')

# Criar a janela principal
janela = tk.Tk()
janela.title('Conversor de Centímetros para Metros')

# Criar e posicionar os widgets
label_instrucao = tk.Label(janela, text='Digite o valor em centímetros:')
label_instrucao.pack(pady=10)

entry_cm = tk.Entry(janela)
entry_cm.pack(pady=10)

botao_converter = tk.Button(janela, text='Converter', command=converter_cm_para_m)
botao_converter.pack(pady=10)

resultado_var = tk.StringVar()
label_resultado = tk.Label(janela, textvariable=resultado_var)
label_resultado.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.mainloop()