import customtkinter as ctk
from sistema import calculando

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

juncao_acima.grid_columnconfigure((0,1), weight=1)
juncao_abaixo.grid_columnconfigure((0,1), weight=1)

# Criar Escritas, as Caixas de Texto e Outros Elementos

tituloapp = ctk.CTkLabel(app, text="Conversor de Moedas", font=("", 36))
subtituloapp = ctk.CTkLabel(app, text="com Python e Custom Tkinter", font=("", 18))
seletor_moeda_origem = ctk.CTkOptionMenu(juncao_acima, values=["BRL - Real","USD - Dolar","EUR - Euro"], width=200)
seletor_moeda_destino = ctk.CTkOptionMenu(juncao_abaixo, values=["BRL - Real","USD - Dolar","EUR - Euro"], width=200)
valor_converter = ctk.CTkEntry(juncao_acima, placeholder_text=" Valor a Converter", fg_color="#2b2b2b", border_width=2, width=200, text_color="white")
valor_convertido = ctk.CTkEntry(juncao_abaixo, placeholder_text=" Valor Convertido", fg_color="#2b2b2b", border_width=2, width=200, text_color="gray")

# Desabilitando a opção de Alteração da Caixa de Resultado da Conversão do Valor

valor_convertido.insert(0, "Valor Convertido")
valor_convertido.configure(state="readonly")

# DEF que calcula/converte as moedas antes de criar o Botao que usa a DEF

def puxando():
    print(calculando)

# Criando o Botao de Converter

botao_converter = ctk.CTkButton(app, text="Converter", command=puxando)

# Colocar os Elementos Criados Acima na Janela do APP usando GRID

tituloapp.grid(row=0, column=0, padx=0, pady=(20,5))
subtituloapp.grid(row=1, column=0, padx=0, pady=(0,15))

juncao_acima.grid(row=2, column=0, sticky="ew", padx=0, pady=20)

seletor_moeda_origem.grid(row=0, column=0, padx=10, pady=5)
valor_converter.grid(row=0, column=1, padx=10, pady=5)

juncao_abaixo.grid(row=3, column=0, sticky="ew", padx=0, pady=20)

seletor_moeda_destino.grid(row=0, column=0, padx=10, pady=5)
valor_convertido.grid(row=0, column=1, padx=10, pady=5)

botao_converter.grid(row=4, column=0, padx=0, pady=(20,5))

# Assinatura

assinatura = ctk.CTkLabel(app, text="github.com/othiagodacruz")
assinatura.grid(row=5, column=0, sticky="ew", padx=0, pady=5)

# Manter a Janela do APP Aberta

app.mainloop()
