import bs4
from bs4 import BeautifulSoup
import csv
import requests
import os
import re


def valuation(value):
    if value <= 200:
        value *= 1.8
    elif value <= 400:  
        value *= 1.7
    elif value <= 600:  
        value *= 1.6
    elif value <= 800:  
        value *= 1.5
    elif value <= 1000:  
        value *= 1.45
    else: 
        value *= 1.4
    return round(value, 2)   

def solveString(string):

  # Obtém o índice do primeiro ponto
  index = string.find(".")

  # Se o índice for positivo, significa que há um ponto na string
  if index >= 0:
    # Recorta a string na posição do ponto
    return string[:index] + string[index + 1:]
  else:
    # Se não há ponto, retorna a string original
    return string


def saving_csv(cdv_data, filename):

    if not os.path.exists("CSVs"):
        os.makedirs("CSVs")

    with open(os.path.join("CSVs", filename), "w", newline="") as csvfile:
        columns = ["Nome", "Preço", "Foto", "Descrição", "Código", "Categoria"]
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for data in cdv_data:
            row = {
                "Nome": data[0],
                "Preço": data[1],
                "Foto": data[2],
                "Descrição": data[3],
                "Código": data[4],
                "Categoria": data[5]
            }

            writer.writerow(row)

def EachProduct(html_file):

    soup = BeautifulSoup(html_file, "html.parser")

    # Obtém todos os elementos da tag `a` com a classe `link-image-servico-v2`
    links = soup.find_all("a", class_="link-image-servico-v2")

    # Cria um vetor para armazenar os links
    links_list = []

    # Percorre todos os elementos da tag `a`
    for link in links:
        # Obtém o atributo `href` do link
        href = link["href"]
        # Adiciona o link ao vetor
        links_list.append(href)

    return links_list


    # links = [a['href'] for a in soup.find_all('a', class_='link-image-servico-v2')]

    # return links

def extractDetails(links):
    textos = []

    for link in links:
        try:
            # Fazendo a requisição para o link
            response = requests.get(link)

            # Verificando se a requisição foi bem-sucedida
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Encontrando a tag desejada e extraindo o texto
                info_servico = soup.find('p', class_='info-servico')
                if info_servico:
                    textos.append(info_servico.text.strip())
                else:
                    textos.append("Tag não encontrada")
            else:
                textos.append("Erro ao acessar o link")
        except Exception as e:
            textos.append(f"Erro ao processar o link: {e}")

    return textos

# Lendo o arquivo HTML externo
def keyWord(link):

  # Obtém a parte do link após o "/categoria/".
  frase_chave = link.split("/categoria/")[1]

  # Remove os espaços em branco da frase chave.
  frase_chave = frase_chave.strip()
  frase_chave = frase_chave.replace("-", " ").replace("/", " ")

  return frase_chave


def filling(subvector):
    vector = []
    for i in subvector:
        vector.append(keyWord(i))
    return vector    
        

def giveLinksTXT(nome_arquivo):
  # Abre o arquivo para leitura.
  arquivo = open(nome_arquivo, "r")
  vetor_links = []

  for linha in arquivo:
    linha = linha.strip()     # Remove os espaços em branco da linha.
    vetor_links.append(linha)
  arquivo.close()

  return vetor_links


def SaveWordKeys(vector):
    # Salvar as palavras chaves corretamente
    arquivo = open("words.txt", "w")

    # Escreve cada string do vetor em uma nova linha do arquivo.
    for string in vector:
        arquivo.write(string + "\n")
    arquivo.close()
    

def OrderedFiles(pasta):
  arquivos = os.listdir(pasta)
  arquivos_ordenados = sorted(arquivos, key=lambda arquivo: int(arquivo.split("_")[0]))
  return arquivos_ordenados


def removeString(string, Ssring):

  pattern = re.compile(Ssring.lower(), re.IGNORECASE)
  new_string = pattern.sub("", string.lower())

  return new_string


def tagsRage(filename, description, cat):

    soup = bs4.BeautifulSoup(filename, "html.parser")

    prices = []
    names = []
    images = []
    uniti = []
    setor = []
    categoria = []
    reference = []

    # Para cada laço, copiar as informações necessárias
    for i in soup.find_all("div", class_="text-left titulo-servico-v2"):
        name = i.text
        names.append(removeString(name, cat));
        
    for i in soup.find_all("span", class_="text-price-v2"):
        price = i.text.split(" ")[0]
        price = price.replace("R$", "")
        price = price.replace(",", ".")
        if(price.count(".") > 1):
            price = solveString(price)
        prices.append(valuation(float(price)))
     

    for i in soup.find_all("img", class_="lozad"):
        img = i.get("data-src")
        images.append(img)

    for i in soup.find_all("span", class_="quantidade_final"):
        quantity = i.find("b").text
        quantity = quantity.replace("unid.", "")
        uniti.append(quantity)

    for i in range(0, len(names)):
        string = f"{uniti[i]} unid - {names[i]}"  
        names[i] = string  
    
    for i in range(0,len(names)):
        categoria.append(cat)

    for tag in soup.find_all("div", class_="titulo-servico-v2"):
        box_info_servico_v2 = []
        for p in tag.find_next_sibling("div", class_="box-info-servico-v2").find_all("p"):
            text = p.text.strip()
            box_info_servico_v2.append(text)    
        reference.append(box_info_servico_v2[1].replace("\xa0", " ").split(" ")[1])
    
    new_texts = []
    pattern_instructions = re.compile("SIGA AS INSTRUÇÕES DO GABARITO ABAIXO.")
    pattern_zap_grafica = re.compile("Zap Gráfica")

    #Trocar as palavras repetidas
    for text in description:
        new_text = pattern_instructions.sub("(ARTE NÃO INCLUSA)", text)
        new_text = pattern_zap_grafica.sub("DelGraf", new_text)
        new_texts.append(new_text)


    cdv_data = list(zip(names, prices, images, new_texts, reference, categoria))
    return cdv_data


pages = giveLinksTXT("links.txt")
WordKeys = filling(pages)

SaveWordKeys(WordKeys)

#Entra no diretório com os arquivos de compra
produtos_compra = OrderedFiles("paid")
produtos_detalhes = OrderedFiles("details")


produtos = []
if len(produtos_compra) == len(produtos_detalhes) == len(WordKeys):
    produtos = list(zip(produtos_compra, produtos_detalhes, WordKeys))

ans = 1
for i in produtos:
    
    with open(os.path.join("paid", i[0]), "r", encoding="utf-8") as file:
        page = file.read()
    with open(os.path.join("details", i[1]), "r", encoding="utf-8") as file:
        info = file.read()    
    productByPage = EachProduct(info)
    description = extractDetails(productByPage)
    data = tagsRage(page, description, i[2])
    print(f"A seção {i[2]} foi completamente registrada")
    saving_csv(data, f"produtos_({i[2]}).csv")
    print("CSV", f"produtos_({i[2]}).csv gerado com sucesso, estamos no arquivo {ans}!")
    ans = ans+1

print("Processo concluído com sucesso!")
