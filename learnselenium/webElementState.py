import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



class WebElementStates:
    def get_element_state(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://training.openspan.com/login")
        demo_state = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state)

        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("mike@gmail.com")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("mike@123")
        time.sleep(2)
        demo_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        time.sleep(4)
        print(demo_state1)


    def get_hidden_element(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        visibility = driver.find_element(By.XPATH, "//div[@id='myDIV']")
        isDisplayed = visibility.is_displayed()
        print(isDisplayed)

        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        time.sleep(2)
        visibility2 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        time.sleep(2)
        print(visibility2)


get_webElement = WebElementStates()
#get_webElement.get_element_state()
get_webElement.get_hidden_element()