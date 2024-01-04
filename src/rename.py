import os

def OrderFiles(pasta, exemplo_arquivo):
    """Ordena e renomeia arquivos em uma pasta, considerando potenciais erros."""

    arquivos = os.listdir(pasta)
    arquivos_ordenados = []

    for arquivo in arquivos:
        try:
            numero = int(arquivo.split("_")[1].split(".")[0])  # Extract number before extension
            arquivos_ordenados.append((numero, arquivo))
        except ValueError:
            print(f"Arquivo '{arquivo}' não segue o formato esperado e será ignorado.")

    arquivos_ordenados.sort()
    arquivos = [arquivo[1] for arquivo in arquivos_ordenados]

    for arquivo in arquivos:
        if arquivo.endswith(".html"):
            numero_pagina = int(arquivo.split("_")[1].split(".")[0])  # Extract number before extension
            novo_arquivo = f"{numero_pagina}_{exemplo_arquivo.split('_')[0]}.html"
            os.rename(os.path.join(pasta, arquivo), os.path.join(pasta, novo_arquivo))

pasta = "paid"
exemplo_arquivo = "compras_1.html"

OrderFiles(pasta, exemplo_arquivo)