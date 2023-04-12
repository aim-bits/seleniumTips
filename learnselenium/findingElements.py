from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class ElementLocator:
    def locate_by_tag_name(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.kippa.africa")
        lista = driver.find_elements(By.TAG_NAME, 'a')
        print(len(lista))
        for i in lista:
            print(i.text)

findBy = ElementLocator()
findBy.locate_by_tag_name()

    