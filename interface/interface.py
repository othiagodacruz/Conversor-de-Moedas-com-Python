import customtkinter as ctk
from sistema.sistema import sistema

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("500x200")
app.title("Conversor de Moedas com Phyton")

valordecima = ctk.CTkEntry(app, placeholder_text="Valor a ser Convertido:")

moedadebaixo = ctk.CTkEntry(app, placeholder_text="Valor Convertido:")

button = ctk.CTkButton(app, text="Converter")
button.pack(pady=5)

app.mainloop()
