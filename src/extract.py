import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = ["https://www.zapgrafica.com.br/loja/produto/categoria/abridores-e-chaveiros/", "https://www.zapgrafica.com.br/loja/produto/categoria/acessorios-para-computadores/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/adesivos/", "https://www.zapgrafica.com.br/loja/produto/categoria/agendas-cadernos-e-apostilas/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/avental/", "https://www.zapgrafica.com.br/loja/produto/categoria/azulejo-decorativo/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/backdrop/", "https://www.zapgrafica.com.br/loja/produto/categoria/balcoes-pdv-quiosques-e-expositores/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/bandeiras/", "https://www.zapgrafica.com.br/loja/produto/categoria/bandeirolas/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/bandeja-de-degustacao/", "https://www.zapgrafica.com.br/loja/produto/categoria/banners-faixas-lonas-e-tecidos/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/baralhos/", "https://www.zapgrafica.com.br/loja/produto/categoria/bastao-de-led/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/bloco-de-post-it/", "https://www.zapgrafica.com.br/loja/produto/categoria/blocos-comandas-receituarios-e-taloes/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/boia-personalizada-decorativa/", "https://www.zapgrafica.com.br/loja/produto/categoria/bottons-e-pins-personalizados/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/brindes/", "https://www.zapgrafica.com.br/loja/produto/categoria/caixas-e-embalagens/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/calendarios-e-folhinhas-2024/", "https://www.zapgrafica.com.br/loja/produto/categoria/camisas-coletes-abadas-e-shorts/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/canecas-e-copos/","https://www.zapgrafica.com.br/loja/produto/categoria/canetas/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/canudos/", "https://www.zapgrafica.com.br/loja/produto/categoria/capa-para-antenas-anti-furto/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/cardapios/", "https://www.zapgrafica.com.br/loja/produto/categoria/carimbos/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/carnes/", "https://www.zapgrafica.com.br/loja/produto/categoria/cartao-de-proximidade/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/cartao-de-vacina/", "https://www.zapgrafica.com.br/loja/produto/categoria/cartazes/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/cartoes-de-visita-europeu/", "https://www.zapgrafica.com.br/loja/produto/categoria/cartoes-de-visita/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/cartoes-duplo/", "https://www.zapgrafica.com.br/loja/produto/categoria/cartoes-fidelidade/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/catalogo-/", "https://www.zapgrafica.com.br/loja/produto/categoria/cd-e-dvd/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/celular-e-acessorios/", "https://www.zapgrafica.com.br/loja/produto/categoria/certificados/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/chinelos-personalizados/", "https://www.zapgrafica.com.br/loja/produto/categoria/cobre-caixas/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/cobre-placa-/", "https://www.zapgrafica.com.br/loja/produto/categoria/combos-de-produtos/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/convites/", "https://www.zapgrafica.com.br/loja/produto/categoria/coqueteleira-para-academia/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/cordoes/", "https://www.zapgrafica.com.br/loja/produto/categoria/cracha/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/credenciais/", "https://www.zapgrafica.com.br/loja/produto/categoria/delivery/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/displays/", "https://www.zapgrafica.com.br/loja/produto/categoria/encarte-tabloides-e-jornal/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/envelopes/", "https://www.zapgrafica.com.br/loja/produto/categoria/espelho/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/estojos-e-necessaires-/", "https://www.zapgrafica.com.br/loja/produto/categoria/facas-corte-vinco/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/ficha/", "https://www.zapgrafica.com.br/loja/produto/categoria/filipetas/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/flagball/", "https://www.zapgrafica.com.br/loja/produto/categoria/folders-e-mala-direta/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/folhas-avulsas/", "https://www.zapgrafica.com.br/loja/produto/categoria/forro-de-bandeja/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/foto-produtos/", "https://www.zapgrafica.com.br/loja/produto/categoria/garrafas-e-squeezes/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/imas-de-geladeira/", "https://www.zapgrafica.com.br/loja/produto/categoria/ingressos-de-seguranca/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/ingressos-de-seguranca/", "https://www.zapgrafica.com.br/loja/produto/categoria/kits-de-mostruario/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/lapis-apontadores-e-giz-de-cera/", "https://www.zapgrafica.com.br/loja/produto/categoria/lixas-de-unha/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/lixeira-para-carro/", "https://www.zapgrafica.com.br/loja/produto/categoria/manta-magnetica-adesivada-03mm/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/marcador-de-pagina/", "https://www.zapgrafica.com.br/loja/produto/categoria/mascaras/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/meia/", "https://www.zapgrafica.com.br/loja/produto/categoria/mini-cartao/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/mini-panfleto/", "https://www.zapgrafica.com.br/loja/produto/categoria/mobile-/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/nao-perturbe/", "https://www.zapgrafica.com.br/loja/produto/categoria/oculos-personalizados/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/outlet-zap/", "https://www.zapgrafica.com.br/loja/produto/categoria/painel-de-festa/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/panfletos-flyers-e-folhetos/", "https://www.zapgrafica.com.br/loja/produto/categoria/papel-timbrado/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/pastas/", "https://www.zapgrafica.com.br/loja/produto/categoria/placa-de-qr-code-pix/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/placa-de-sinalizacao-pvc-/","https://www.zapgrafica.com.br/loja/produto/categoria/porta-caneca-alca-/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/porta-copos/", "https://www.zapgrafica.com.br/loja/produto/categoria/porta-documentos/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/postais/", "https://www.zapgrafica.com.br/loja/produto/categoria/poster/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/produtos-para-festa-/", "https://www.zapgrafica.com.br/loja/produto/categoria/produtos-sem-personalizacao/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/projeto-arquitetonico/", "https://www.zapgrafica.com.br/loja/produto/categoria/pulseiras/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/quadros-decorativos/", "https://www.zapgrafica.com.br/loja/produto/categoria/quebra-cabeca-imantado/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/reguas/", "https://www.zapgrafica.com.br/loja/produto/categoria/revista/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/rifa/", "https://www.zapgrafica.com.br/loja/produto/categoria/rotulo-bobina/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/rotulos/", "https://www.zapgrafica.com.br/loja/produto/categoria/sacolas-e-sacos/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/tabua-de-vidro/", "https://www.zapgrafica.com.br/loja/produto/categoria/tags/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/tapetes-e-capachos/", "https://www.zapgrafica.com.br/loja/produto/categoria/topo-para-bomba-de-gasolina/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/trena/", "https://www.zapgrafica.com.br/loja/produto/categoria/ventarola/", 
       "https://www.zapgrafica.com.br/loja/produto/categoria/viseiras/", "https://www.zapgrafica.com.br/loja/produto/categoria/wind-banner/",
       "https://www.zapgrafica.com.br/loja/produto/categoria/wobbler/", "https://www.zapgrafica.com.br/loja/produto/categoria/x-banner/"]

print(f"Será feita a lsitagem de produtos em {len(url)} páginas")

contador = 1

def extracting(url, nome_arquivo):
    try:
        # Faz a requisição para o site
        resposta = requests.get(url)
        os.makedirs("details", exist_ok=True)
        # Verifica se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            # Usa a função `os.path.join()` para combinar o caminho do diretório com o nome do arquivo.
            with open(os.path.join("details", nome_arquivo), 'w', encoding='utf-8') as arquivo:
                arquivo.write(resposta.text)
            return f"HTML salvo com sucesso em details"
        else:
            return f"Erro ao acessar o site: Status code {resposta.status_code}"
    except requests.RequestException as e:
        return f"Erro ao acessar o site: {e}"

def saveTXT(vetor, nome_arquivo):

  # Abre o arquivo para escrita.
  arquivo = open(nome_arquivo, "w")

  # Escreve cada string do vetor em uma nova linha do arquivo.
  for string in vetor:
    arquivo.write(string + "\n")

  # Fecha o arquivo.
  arquivo.close()


for url in url:
    # inicializa o edge
    driver = webdriver.Edge()
    # Abre o site desejado
    driver.get(url)

    # Espera 5 segundos para que o site carregue
    # body = driver.find_element_by_tag_name('body')

    body = driver.find_element(By.TAG_NAME, 'body')


    for i in range(0,50):
        body.send_keys(Keys.PAGE_DOWN)
        # Pausa entre scrolls (ajuste conforme necessário)
        time.sleep(0.1)

    html = driver.page_source

    nome_arquivo = f"detalhes_{contador}.html"  # Nome do arquivo onde o HTML será salvo
    resultado = extracting(url, nome_arquivo)

    botao_entre = driver.find_element(By.ID, 'hoverDropdown')
    botao_entre.click()

    # Substitua 'campo_usuario' e 'campo_senha' pelos seletores corretos dos campos de usuário e senha
    username_field = driver.find_element(By.ID, 'input-home1-email')
    username_field.send_keys('')

    password_field = driver.find_element(By.ID, 'input-home1-senha')
    password_field.send_keys('')

    #Clica em login
    login_button = driver.find_element(By.ID, 'btnEntrarHome')
    login_button.click()

    time.sleep(5)
    driver.refresh()
    
    #Pega o HTML com todos os produtos
    body = driver.find_element(By.TAG_NAME, 'body')


    for i in range(0,50):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    html = driver.page_source

    driver.close()

    os.makedirs("paid", exist_ok=True)

    with open(os.path.join("paid", f"compras_{contador}.html"), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Compras_{contador} salvo com sucesso | url: {url}\n")    
    # Obtém o HTML do site

    contador = contador + 1

saveTXT(url, "links.txt")
# Salva o HTML em um arquivo .html

# Fecha o navegador


# Exemplo de uso
print("Extração de ambos concluídas com sucesso")

