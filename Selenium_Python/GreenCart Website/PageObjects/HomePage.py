import time
from selenium.webdriver.common.by import By


class HomePageObject:

    def __init__(self, driver):
        self.driver = driver

    def redirectHomePage(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        self.driver.maximize_window()

    def assertHomePage(self):
        #assert driver.find_element(By.CLASS_NAME, "brand greenLogo").text == "GREEN"
        assert self.driver.find_element(By.CLASS_NAME, "redLogo").text == "KART"

    def assertSearchFunctionailtyAndAddItems(self):
        self.driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("Nuts")
        time.sleep(5)
        #driver.find_element(By.CLASS_NAME, "search-button").click()
        items = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        print(len(items))
        #driver.find_element(By.XPATH, "(//a[@class ='increment'])[1]").click()
        #print(items[0].find_element(By.XPATH, "//h4").text)

        for item in items:
            item.find_element(By.XPATH, "//a[@class='increment']").click()
            # print(item.find_element(By.XPATH, "//h4").text)
            assert (item.find_element(By.XPATH, "//h4").text.lower().__contains__("nuts"))
            item.find_element(By.XPATH, "div/button").click()

    def proceedToCheckout(self):
        self.driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
        self.driver.find_element(By.CLASS_NAME, "action-block").click()

    def assertHomePage(self):
        assert self.driver.find_element(By.CLASS_NAME, "search-keyword").is_displayed()
