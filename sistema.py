import json

def converter(valor, moeda_origem, moeda_destino):

    open (valores)
    valores = json.load(arquivo)
    
    taxa_origem = valores[moeda_origem]
    taxa_destino = valores[moeda_destino]

    convertendo = valor * taxa_origem / taxa_destino

    return(convertendo)

print(converter(100, "real", "dolar_americano"))
print(json)