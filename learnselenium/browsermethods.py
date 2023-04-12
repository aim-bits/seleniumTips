from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Browser_methods:
    def browser_methods():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.kippa.africa")
        print(driver.title)
        driver.maximize_window()
        print(driver.current_url)
        driver.refresh()
        driver.fullscreen_window()
        

demo_browser_method = Browser_methods()
demo_browser_method.browser_methods
