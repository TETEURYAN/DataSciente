import csv


# def alterar_casa_decimal(arquivo_csv, coluna_preco):
#   """
#   Altera a casa decimal de todos os itens da coluna preço de um arquivo csv.

#   Args:
#     arquivo_csv: O caminho do arquivo csv a ser alterado.
#     coluna_preco: O nome da coluna de preço do arquivo csv.

#   Returns:
#     None.
#   """

#   with open(arquivo_csv, "r", encoding="utf-8") as arquivo:
#     reader = csv.reader(arquivo, delimiter=",")
#     header = next(reader)
#     indice_coluna_preco = header.index(coluna_preco)
#     linhas = list(reader)  # Armazena as linhas em uma lista

#   for linha in linhas:
#     if len(linha) == 0:  # Verifica se a linha está vazia
#       print(f"Linha vazia: {linha}")
#       continue

#     preco = linha[indice_coluna_preco]
#     preco_split = preco.split(".")
#     preco_sem_centavos = preco_split[:-1]
#     preco = ".".join(preco_sem_centavos) + ".90"
#     linha[indice_coluna_preco] = preco

#     nome = linha[0]
#     nome_split = nome.split("-")
#     nome_primeira_letra_maiuscula = "- ".join([nome_split[0].capitalize()] + nome_split[1:])
#     linha[0] = nome_primeira_letra_maiuscula

#   with open(arquivo_csv, "w", encoding="utf-8") as arquivo:
#     writer = csv.writer(arquivo, delimiter=",")
#     writer.writerow(header)
#     writer.writerows(linhas)  # Escreve as linhas armazenadas

# if __name__ == "__main__":
#   arquivo_csv = "resultado/resultado.csv"
#   coluna_preco = "Preço"

#   alterar_casa_decimal(arquivo_csv, coluna_preco)


# import os
# import csv

# import os
# import csv

# def juntar_csv(pasta):
#   """
#   Junta todos os arquivos .csv em uma pasta em um único arquivo .csv.

#   Args:
#     pasta: O caminho para a pasta que contém os arquivos .csv.

#   Returns:
#     O caminho para o arquivo .csv resultante.
#   """

#   # Obtém uma lista de todos os arquivos .csv na pasta
#   arquivos_csv = [os.path.join(pasta, arquivo) for arquivo in os.listdir(pasta) if arquivo.endswith(".csv")]

#   # Cria o diretório para o arquivo .csv resultante
#   os.makedirs("resultado", exist_ok=True)

#   # Abre o arquivo .csv resultante em modo de escrita
#   with open("resultado/resultado.csv", "w", newline="", encoding="utf-8") as f:  # Especificando a codificação utf-8
#     writer = csv.writer(f, delimiter=",")

#     # Itera sobre todos os arquivos .csv
#     for arquivo_csv in arquivos_csv:
#       try:
#         # Tenta abrir o arquivo com a codificação utf-8
#         with open(arquivo_csv, "r", encoding="utf-8") as f_csv:
#           reader = csv.reader(f_csv, delimiter=",")

#           # Adiciona as linhas do arquivo atual ao arquivo resultante
#           for linha in reader:
#             writer.writerow(linha)

#       except UnicodeDecodeError:
#         # Se a codificação utf-8 não funcionar, tente com latin-1
#         try:
#           with open(arquivo_csv, "r", encoding="latin-1") as f_csv:
#             reader = csv.reader(f_csv, delimiter=",")

#             # Adiciona as linhas do arquivo atual ao arquivo resultante
#             for linha in reader:
#               writer.writerow(linha)

#         except UnicodeDecodeError:
#           print(f"Erro de codificação no arquivo {arquivo_csv}")

#   return "resultado/resultado.csv"


# pasta = "CSVs"

# arquivo_csv = juntar_csv(pasta)

import csv

import csv

import csv

def remover_linhas_em_branco_descricao(arquivo_csv):
  """
  Remove todas as linhas em branco da coluna "Descrição" de um arquivo .csv.

  Args:
    arquivo_csv: O caminho para o arquivo .csv a ser alterado.

  Returns:
    O arquivo .csv alterado.
  """

  with open(arquivo_csv, "r", encoding="utf-8",) as f:
    reader = csv.reader(f, delimiter=",")

    # Obtém uma lista de todas as linhas do arquivo, sem linhas em branco na coluna "Descrição"
    linhas = []
    for linha in reader:
      if linha[2]:
        linhas.append(linha)

  with open(arquivo_csv, "w", newline="", encoding="utf-8",) as f:
    writer = csv.writer(f, delimiter=",")

    # Escreve as linhas no arquivo alterado
    writer.writerows(linhas)

  return arquivo_csv



arquivo_csv = "resultado/resultado.csv"

arquivo_csv = remover_linhas_em_branco_descricao(arquivo_csv)
