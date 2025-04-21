import time
from datetime import datetime

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePageObject
from PageObjects.CheckoutPage import CheckOutPageObject

current_time = datetime.now()

driver = webdriver.Chrome()
driver.implicitly_wait(5)

homePage = HomePageObject(driver)
checkOutPage = CheckOutPageObject(driver)

homePage.redirectHomePage()
homePage.assertHomePage()
homePage.assertSearchFunctionailtyAndAddItems()
homePage.proceedToCheckout()

Total_Amount = checkOutPage.assertCartTotal()
checkOutPage.applyCouponAndAssertReducedTotal(Total_Amount)

checkOutPage.verifyCountryAndPlaceOrder()
homePage.assertHomePage()

