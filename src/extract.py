import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options


driver = webdriver.Edge()
driver.get("https://www.zapgrafica.com.br/loja/home/categoria/abridores-e-chaveiros/")

# Gap de tempo
time.sleep(130)

# Obtém o HTML do site
html = driver.page_source

# Salva o HTML em um arquivo .html
with open("google.html", "w") as f:
    f.write(html)

# Fecha o navegador
driver.close()
