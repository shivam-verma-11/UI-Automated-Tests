from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckOutPageObject:

    def __init__(self, driver):
        self.driver = driver

    def assertCartTotal(self):
        Sum = 0
        Item_Total = self.driver.find_elements(By.CSS_SELECTOR, "tbody td:nth-child(5)")
        for cost in Item_Total:
            Sum = Sum + int(cost.text)

        Total_Amount = int(self.driver.find_element(By.CLASS_NAME, "totAmt").text)
        assert Sum == Total_Amount
        return Total_Amount

    def applyCouponAndAssertReducedTotal(self, Total_Amount):
        assert self.driver.find_element(By.CLASS_NAME, "discountPerc").text == "0%"
        self.driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
        self.driver.find_element(By.CLASS_NAME, "promoBtn").click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "promoInfo")))
        assert self.driver.find_element(By.CLASS_NAME, "promoInfo").text.__contains__("Code applied")
        assert self.driver.find_element(By.CLASS_NAME, "discountPerc").text == "10%"
        Total_After_Discount = int(self.driver.find_element(By.CLASS_NAME, "discountAmt").text)
        assert Total_After_Discount == 0.9 * Total_Amount

    def verifyCountryAndPlaceOrder(self):
        self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[class='wrapperTwo'] select option[value='India']").click()
        self.driver.find_element(By.CLASS_NAME, "chkAgree").click()
        self.driver.find_element(By.XPATH, "//button[text()='Proceed']").click()

        