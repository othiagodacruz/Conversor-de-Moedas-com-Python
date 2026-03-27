# Importar o CTK que usamos no Layout da interface e mais duas DEF lá do sistema

import customtkinter as ctk
from sistema import calculando
from sistema import carregar_valores

# Definir o tema do CustomTkinter

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Criar a Janela do APP, Definir o Tamanho e o Titulo da Janela 

app = ctk.CTk()
app.geometry("500x360")
app.title("Conversor de Moedas com Phyton")

# Definindo a Centralização da Janela

app.grid_columnconfigure(0, weight=1)

# Criando Campos e Centralizando eles dentro da Janela do APP para Organizar LADO A LADO

juncao_acima = ctk.CTkFrame(app, fg_color="transparent")
juncao_abaixo = ctk.CTkFrame(app, fg_color="transparent")

juncao_acima.grid_columnconfigure((0,1,2), weight=1)
juncao_abaixo.grid_columnconfigure((0,1,2), weight=1)

# Puxar os nomes das Moedas da Lista JSON que foi convertida la no Sistema

lista_json = carregar_valores()
tipos_moedas = list(lista_json.keys())

# DEF que atualiza os Simbolos das Moedas de Origem

def atualizar_simbolo_origem(_=None):
    moeda = seletor_moeda_origem.get()
    simbolo = lista_json[moeda]["simbolo"]
    simbolo_origem.configure(text=simbolo)

# DEF que atualiza os Simbolos das Moedas de Destino

def atualizar_simbolo_destino(_=None):
    moeda = seletor_moeda_destino.get()
    simbolo = lista_json[moeda]["simbolo"]
    simbolo_destino.configure(text=simbolo)

# Criar Escritas, as Caixas de Texto e Outros Elementos

tituloapp = ctk.CTkLabel(app, text="Conversor de Moedas", font=("", 36))
subtituloapp = ctk.CTkLabel(app, text="com Python e Custom Tkinter", font=("", 18))

seletor_moeda_origem = ctk.CTkOptionMenu(juncao_acima, values=tipos_moedas, width=200, command=atualizar_simbolo_origem)
simbolo_origem = ctk.CTkLabel(juncao_acima, text="")
seletor_moeda_origem.set(tipos_moedas[0])

seletor_moeda_destino = ctk.CTkOptionMenu(juncao_abaixo, values=tipos_moedas, width=200, command=atualizar_simbolo_destino)
simbolo_destino = ctk.CTkLabel(juncao_abaixo, text="")
seletor_moeda_destino.set(tipos_moedas[1])

valor_converter = ctk.CTkEntry(juncao_acima, placeholder_text=" Valor a Converter", fg_color="#2b2b2b", border_width=2, width=200, text_color="white")
valor_convertido = ctk.CTkEntry(juncao_abaixo, placeholder_text=" Valor Convertido", fg_color="#2b2b2b", border_width=2, width=200, text_color="gray")

# Travando a opção de Alteração na Caixa de Resultado da Conversão do Valor

valor_convertido.insert(0, "Valor Convertido")
valor_convertido.configure(state="readonly")

# DEF que calcula/converte as moedas antes de criar o Botao que usa a DEF

def puxando():

    # Transformando os dados de cima para usar na DEF

    resvalor_converter = float(valor_converter.get())
    resseletor_moeda_origem = seletor_moeda_origem.get()
    resseletor_moeda_destino = seletor_moeda_destino.get()

    # Executa o calculo da função...

    resultado = calculando(resvalor_converter, resseletor_moeda_origem, resseletor_moeda_destino)

    # Destravar a Caixa de Resultado para dar o Valor Convertido e após o resultado, Travar novamente

    valor_convertido.configure(state="normal")
    valor_convertido.delete(0, "end")

    valor_convertido.insert(0, f"{resultado:.2f}")

    valor_convertido.configure(state="readonly")

# Criando o Botao de Converter

botao_converter = ctk.CTkButton(app, text="Converter", command=puxando)

# Colocar os Elementos Criados Acima na Janela do APP usando GRID

tituloapp.grid(row=0, column=0, padx=0, pady=(20,5))
subtituloapp.grid(row=1, column=0, padx=0, pady=(0,15))

juncao_acima.grid(row=2, column=0, sticky="ew", padx=0, pady=20)

seletor_moeda_origem.grid(row=0, column=0, padx=10, pady=5)
simbolo_origem.grid(row=0, column=1, padx=5, pady=5)
valor_converter.grid(row=0, column=2, padx=10, pady=5)

juncao_abaixo.grid(row=3, column=0, sticky="ew", padx=0, pady=20)

seletor_moeda_destino.grid(row=0, column=0, padx=10, pady=5)
simbolo_destino.grid(row=0, column=1, padx=5, pady=5)
valor_convertido.grid(row=0, column=2, padx=10, pady=5)

botao_converter.grid(row=4, column=0, padx=0, pady=(20,5))

# Definir e Exibir a Moeda Iniciar e Final ao abrir o APP
 
moeda_inicial = seletor_moeda_origem.get()
atualizar_simbolo_origem(moeda_inicial)

moeda_final = seletor_moeda_destino.get()
atualizar_simbolo_destino(moeda_final)

# Assinatura

assinatura = ctk.CTkLabel(app, text="github.com/othiagodacruz")
assinatura.grid(row=5, column=0, sticky="ew", padx=0, pady=5)

# Manter a Janela do APP Aberta

app.mainloop()
