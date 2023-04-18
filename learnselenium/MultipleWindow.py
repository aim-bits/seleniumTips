from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class MultipleWindows:
    def demo_windows(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://kippa.africa/")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//section[@class='relative overflow-hidden']//div[@class='flex flex-wrap -mx-4']").click()
        all_handles = driver.window_handles
        print(all_handles)

        for handle in all_handles:
            if handle != all_handles:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[normalize-space()='OPEN A BUSINESS BANK ACCOUNT']")
                time.sleep(4)
                driver.close()
                time.sleep(2)
                break

        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH,
                            "//section[@class='relative overflow-hidden']//div[@class='flex flex-wrap -mx-4']").click()


dmultiplewindows = MultipleWindows()
dmultiplewindows.demo_windows()
        # all_handles = driver.window_handles
        # print(all_handles)
        #
        # for handle in all_handles:
