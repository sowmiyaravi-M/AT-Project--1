from selenium.webdriver.common.by import By

class WebLocators:

   def __init__(self):
       self.usernameLocator = "username"
       self.passwordLocator = "password"
       self.buttonLocator = "button"
       self.PIMLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'

   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.NAME, value=locator).send_keys(textValue)

   def text(self, driver, locator, textValue):
       driver.find_element(by=By.XPATH, value=locator).send_keys(textValue)

   def clickButton(self, driver, locator):
       driver.find_element(by=By.TAG_NAME, value=locator).click()

   def click(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()


