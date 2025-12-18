from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'
browser = Firefox()
browser.get(url)

sleep(0.5)

a = browser.find_element(By.TAG_NAME, 'a')
#p = browser.find_elements(By.TAG_NAME, 'p')

for click in range(11):
    p = browser.find_elements(By.TAG_NAME, 'p')
    a.click()
    print(p[-1].text)