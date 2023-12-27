import bs4
import csv

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

def tagsRage(filename):
    with open(filename, "r") as f:
        html = f.read()

    soup = bs4.BeautifulSoup(html, "html.parser")

    prices = []
    names = []
    images = []
    uniti = []
    setor = []
    categoria = []
    reference = []


    for i in soup.find_all("div", class_="text-left titulo-servico-v2"):
        name = i.text
        name = name.replace("Abridores E Chaveiros", "").strip()
        names.append(name);
        
    for i in soup.find_all("span", class_="text-price-v2"):
        price = i.text.split(" ")[0]
        price = price.replace("R$", "")
        price = price.replace(",", ".")
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
    
    string = "Abridores E Chaveiros"
    for i in range(0,len(names)):
        setor.append(string)
        categoria.append(string)

    for tag in soup.find_all("div", class_="titulo-servico-v2"):
        box_info_servico_v2 = []
        for p in tag.find_next_sibling("div", class_="box-info-servico-v2").find_all("p"):
            text = p.text.strip()
            box_info_servico_v2.append(text)    
        reference.append(box_info_servico_v2[1].replace("\xa0", " ").split(" ")[1])

    cdv_data = list(zip(names, prices, images, setor, reference, categoria))
    return cdv_data

def saving_csv(cdv_data, filename):
    with open(filename, "w", newline="") as csvfile:
        columns = ["Nome", "Preço", "Foto", "Descrição", "Código", "Categoria","Embalagem-Largura","Embalagem-Altura", "Embalagem-Comprimento", "Embalagem-Peso", "Embalagem-Transporte", "Estoque-Saldo", "Variacao1", "Variavel1", "Variacao2", "Variavel2", "Variacao3", "Variavel3", "Variacao4", "Variavel4"]
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for data in cdv_data:
            row = {
                "Nome": data[0],
                "Preço": data[1],
                "Foto": data[2],
                "Descrição": data[3],
                "Código": data[4],
                "Categoria": data[5],
                "Embalagem-Largura": "",
                "Embalagem-Altura": "",
                "Embalagem-Comprimento": "",
                "Embalagem-Peso" : "", 
                "Embalagem-Transporte" : "",
                "Estoque-Saldo" : "",
                "Variacao1": "", 
                "Variavel1" : "",
                "Variacao2" : "", 
                "Variavel2" : "", 
                "Variacao3" : "", 
                "Variavel3" : "",
                "Variacao4" : "", 
                "Variavel4" : ""
            }

            writer.writerow(row)

# Lendo o arquivo HTML externo
filename = "teste.html"
data = tagsRage(filename)
saving_csv(data, "produtos01.csv")

print("Codigo executado com sucesso!")






