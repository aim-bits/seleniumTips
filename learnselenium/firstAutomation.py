from selenium import webdriver
from selenium.webdriver.chrome.service import Service



browser = webdriver.Chrome(executable_path="/home/aim/BrowserDrivers/chromedriver")
browser.get("https://www.google.com")


