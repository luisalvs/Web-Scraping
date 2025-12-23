from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Firefox()
browser.get(url)

sleep(0.3)

elementos = browser.find_elements(By.CSS_SELECTOR, 'p[atributo]')
dict = {}

for e in elementos:
    chave = e.get_attribute('atributo')
    valor = e.text
    dict[chave] = valor

print(dict)

browser.quit()