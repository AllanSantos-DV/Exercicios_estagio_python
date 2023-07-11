import io
import sys
import tkinter as tk
from tkinter import scrolledtext

import Funcoes
import FuncoesTest

inputInvalido = "Entrada inválida"


def executar_exercicio():
    opcao_selecionada = opcao_var.get()
    string_input = input_text.get()
    if Funcoes.validar_entrada(string_input):
        output_text_config(inputInvalido)
    else:
        resultados = [item["funcao"](string_input) for item in opcoes if item["opcao"] == opcao_selecionada]
        output_text_config(resultados[0])


def output_text_config(valor):
    output_text.configure(state="normal", width=50)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, valor)
    output_text.configure(state="disabled")

    if len(valor) > 30:
        output_text.configure(wrap=tk.NONE)
        scrollbar_horizontal.pack(side="bottom", fill="x")
    else:
        output_text.configure(wrap=tk.WORD)
        scrollbar_horizontal.pack_forget()


def executar_testes_unittest():
    output_stream = io.StringIO()
    sys.stdout = output_stream

    suite = FuncoesTest.unittest.TestLoader().loadTestsFromModule(FuncoesTest)
    FuncoesTest.unittest.TextTestRunner(stream=output_stream, verbosity=2).run(suite)

    sys.stdout = sys.__stdout__

    output = output_stream.getvalue()
    janela_testes = tk.Toplevel(janela)
    janela_testes.title("Resultados dos Testes com Unittest")

    output_text_testes = scrolledtext.ScrolledText(janela_testes, state="normal", width=100, height=20)
    output_text_testes.insert(tk.END, output)
    output_text_testes.configure(state="disabled")
    output_text_testes.pack(pady=5, padx=5)


# Cria a janela
janela = tk.Tk()
janela.title("Manipulação de Strings")

# Configuração da janela
width_app = 600
height_app = 300

# Centralizando na tela
pos_x = (janela.winfo_screenwidth() - width_app) // 2
pos_y = (janela.winfo_screenheight() - height_app) // 2
janela.geometry(f"{width_app}x{height_app}+{pos_x}+{pos_y}")

# Rotulo para seleção do exercicio
exercicio_label = tk.Label(janela, text="Selecione um exercício:")
exercicio_label.pack()

# Lista de opções
opcoes = [
    {"opcao": "Inverter Palavras", "funcao": Funcoes.inverter_palavras},
    {"opcao": "Remover Duplicados", "funcao": Funcoes.remover_duplicados},
    {"opcao": "Maior Palindromo", "funcao": Funcoes.maior_palindromo},
    {"opcao": "Formatar Frase", "funcao": Funcoes.formatar_frase},
    {"opcao": "Anagrama Palindromo", "funcao": Funcoes.anagrama_palindromo}
]

# Variável para armazenar a opção selecionada
opcao_var = tk.StringVar(janela)
opcao_var.set(opcoes[0]["opcao"])

# Criar o widget OptionMenu
menu_exercicios = tk.OptionMenu(janela, opcao_var, *[item["opcao"] for item in opcoes])
menu_exercicios.pack(pady=(0, 10))

# Rotulo para entrada
input_label = tk.Label(janela, text="Digite a String (Frase ou Palavra): ")
input_label.pack()

input_text = tk.Entry(janela, width=50)
input_text.pack(pady=(0, 10))

button_executar = tk.Button(janela, text="Executar", command=executar_exercicio)
button_executar.pack(pady=(0, 10))

# Criar um Frame para agrupar o output_text e a barra de rolagem
frame_output = tk.Frame(janela)
frame_output.pack(pady=(0, 10))

output_text = tk.Text(frame_output, width=50, height=1)
output_text.configure(state="disabled", font=("Arial", 12))
output_text.pack(side="top")

# Criar a barra de rolagem horizontal
scrollbar_horizontal = tk.Scrollbar(frame_output, orient="horizontal", command=output_text.xview)
output_text.configure(xscrollcommand=scrollbar_horizontal.set)

button_executar_testes = tk.Button(janela, text="Executar Testes Unittest", command=executar_testes_unittest)
button_executar_testes.pack()

janela.mainloop()
