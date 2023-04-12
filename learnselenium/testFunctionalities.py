import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Functionalities:
    def get_element_text(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.kippa.africa")
        tes= driver.find_element(By.XPATH, "//button[normalize-space()='Webinar']")
        print(tes.text)
        
    def get_attibute_value(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.kippa.africa")
        att_val= driver.find_element(By.XPATH, "//h1[normalize-space()='Resources to help your business succeed']").get_attribute("class")
        print(att_val)

findBy = Test_Functionalities()
findBy.get_attibute_value()