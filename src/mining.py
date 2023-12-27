import bs4

def extract_data_all_tags(filename):
    with open(filename, "r") as f:
        html = f.read()

    soup = bs4.BeautifulSoup(html, "html.parser")

    all_data = []  # Store data for all tags

    for tag in soup.find_all("div", class_="titulo-servico-v2"):
        nome = tag.text
        nome = nome.replace("Abridores E Chaveiros", "").strip()

        valor = tag.find_next_sibling("span", class_="text-price-v2")
        price = valor.text if valor else ""

        setor = "Abridores E Chaveiros"
        unit_tag = tag.find_next_sibling("span", class_="quantidade_final")
        unit = unit_tag.get_text() if unit_tag else ""
        unit = unit.strip().split(" ", 1)[0]
        unidade = f"{unit[:2]}{unit[2:]} unid -"
        name = f"{unidade} {nome}"

        box_info_servico_v2 = []
        for p in tag.find_next_sibling("div", class_="box-info-servico-v2").find_all("p"):
            text = p.text.strip()
            box_info_servico_v2.append(text)

        reference = box_info_servico_v2[1].replace("\xa0", " ")
        image_tag = tag.find_next_sibling("img", class_="lozad")
        image = image_tag.get("data-src") if image_tag else ""

        data = {
            "nome": name,
            "preco": price,
            "imagem": image,
            "descricao": setor,
            "codigo": reference,
            "categoria": setor
        }
        all_data.append(data)

    return all_data
# Lendo o arquivo HTML externo
filename = "teste.html"
data = extract_data_all_tags(filename)

for i in data:
    print(i)
    print("\n")

print(len(data))    

