from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time 

class ElementLocator():
    def locate_by_name(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        driver.find_element(By.NAME, 'q').send_keys("Hello")
        time.sleep(4)
        
    def locate_by_xpath(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        driver.find_element(By.XPATH, "//input[@title='Search']").send_keys("Hello")
        time.sleep(4)
        
    def locate_by_css_selector(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        driver.find_element(By.CSS_SELECTOR, "input[title='Search']").send_keys("Hello")
        time.sleep(4)
    
    def locate_by_link_text(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        driver.find_element(By.LINK_TEXT, "Images").click()
        #driver.find_element(By.LOCATOR "web-element").ACTION
        time.sleep(2)
        
    def locate_by_class_name(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.google.com/")
        driver.find_element(By.CLASS_NAME, "gb_q").click()
        time.sleep(3)
    
        
        
findby = ElementLocator()
# findby.locate_by_name()      
# findby.locate_by_xpath()
#findby.locate_by_css_selector()
findby.locate_by_link_text()
findby.locate_by_class_name()


        