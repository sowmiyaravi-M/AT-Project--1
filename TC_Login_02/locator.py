from selenium.webdriver.common.by import By
class WebLocators:

   def __init__(self):
       self.usernameLocator = "username"
       self.passwordLocator = "password"
       self.buttonLocator = "button"


   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.NAME ,value=locator).send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.TAG_NAME, value=locator).click()


