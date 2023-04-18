from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class ButtonsXboxes:
    def checkboxes(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")

        driver.find_element(By.ID, "doi0]").click()
        time.sleep(4)
        checkSelection = driver.find_element(By.ID, "doi0']").is_selected()
        print(checkSelection)


demo_buttonXboxes = ButtonsXboxes()
demo_buttonXboxes.checkboxes()