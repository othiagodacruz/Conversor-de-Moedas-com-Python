import json

def carregar_valores():
    with open("dados/valoresconversao.json", "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def calculando(valor, moeda_origem, moeda_destino):
    valores = carregar_valores()

    taxa_origem = valores[moeda_origem]
    taxa_destino = valores[moeda_destino]

    resultado = valor * taxa_origem / taxa_destino
    return resultado