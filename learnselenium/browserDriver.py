from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

broswer1 = webdriver.Chrome(ChromeDriverManager().install())
browser2 = webdriver.Firefox(Service = GeckoDriverManager().install())
browser2.get("https://www.rcvacademy.com")
time.sleep(5)
broswer1.get("https://www.rcvacademy.com")
time.sleep(5)
print(broswer1.title)
time.sleep(5)
broswer1.close()