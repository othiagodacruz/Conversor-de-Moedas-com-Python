# Importando JSON (onde tem os nomes e valores das Moedas)

import json

# DEF que carrega os valores do JSON como leitura e formata para o Python

def carregar_valores():
    with open("dados/valoresconversao.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

# DEF que é usada na Interface para efetuar os Calculos da Conversão

def calculando(valor, moeda_origem, moeda_destino):
    valores = carregar_valores()

    taxa_origem = valores[moeda_origem]["taxa"]
    taxa_destino = valores[moeda_destino]["taxa"]

    resultado = valor * taxa_origem / taxa_destino
    return resultado