import customtkinter as ctk
import sistema

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("300x600")
app.title("Conversor de Moedas com Phyton")

moedas = sistema.carregar_moedas()

moedadecima = ctk.StringVar(app, value="Moeda: ")
moedadebaixo = ctk.StringVar(app, value="Moeda: ")

seletordecima = ctk.CTkOptionMenu(app, values=moedas, variable=moedadecima)
valordecima = ctk.CTkEntry(app, placeholder_text="Valor a ser Convertido: ")

def convertendo():  

    valor = valordecima.get()
    origem = moedadecima.get()
    destino = moedadebaixo.get()

    resultado = sistema.converter(valor, origem, destino)
    return(resultado)

seletordebaixo = ctk.CTkOptionMenu(app, values=moedas, variable=moedadebaixo)
valorebaixo = ctk.CTkEntry(app, placeholder_text="Valor Convertido: ")

button = ctk.CTkButton(app, text="Converter", command=convertendo)
button.pack(pady=5)

app.mainloop()
