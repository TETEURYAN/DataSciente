import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.zapgrafica.com.br/loja/home/categoria/abridores-e-chaveiros/"  # Substitua pela URL desejada



def extracting(url, nome_arquivo):
    try:
        # Faz a requisição para o site
        resposta = requests.get(url)

        # Verifica se a requisição foi bem-sucedida
        if resposta.status_code == 200:
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.write(resposta.text)
            return f"HTML salvo com sucesso em {nome_arquivo}"

# inicializa o edge
driver = webdriver.Edge()
# Abre o site desejado
driver.get(url)
html = driver.page_source

# Espera 5 segundos para que o site carregue
# body = driver.find_element_by_tag_name('body')

body = driver.find_element(By.TAG_NAME, 'body')


for i in range(0,50):
    body.send_keys(Keys.PAGE_DOWN)
    # Pausa entre scrolls (ajuste conforme necessário)
    time.sleep(0.2)

nome_arquivo = "detalhes.html"  # Nome do arquivo onde o HTML será salvo
resultado = extracting(url, nome_arquivo)

botao_entre = driver.find_element(By.ID, 'hoverDropdown')
botao_entre.click()

# Substitua 'campo_usuario' e 'campo_senha' pelos seletores corretos dos campos de usuário e senha
username_field = driver.find_element(By.ID, 'input-home1-email')
username_field.send_keys('')

password_field = driver.find_element(By.ID, 'input-home1-senha')
password_field.send_keys('')

# Substitua 'botao_login' pelo seletor correto do botão de login
login_button = driver.find_element(By.ID, 'btnEntrarHome')
login_button.click()

time.sleep(5)
driver.refresh()
body = driver.find_element(By.TAG_NAME, 'body')


for i in range(0,100):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    
# Fecha o navegador
driver.close()

# Salva o HTML em um arquivo .html
with open("compras.html", "w") as f:
    f.write(html)





# Exemplo de uso
print("Extração de ambos concluídas com sucesso")




