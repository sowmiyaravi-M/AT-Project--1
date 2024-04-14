from selenium.webdriver.common.by import By
class WebLocators:

   def __init__(self):
       self.usernameLocator = "username"
       self.passwordLocator = "password"
       self.buttonLocator = "button"
       self.PIMLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
       self.addLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
       self.firstNameLocator = "firstName"
       self.lastNameLocator = "lastName"
       self.saveLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
       self.middleNameLocator = "middleName"
       self.IDLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
       self.licenseLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
       self.expiryDateLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
       self.dobLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
       self.SaveLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'



   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.NAME ,value=locator).send_keys(textValue)

   def text(self, driver, locator, textValue):
       driver.find_element(by=By.XPATH ,value=locator).send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.TAG_NAME, value=locator).click()

   def click(self, driver, locator):
       driver.find_element(by=By.XPATH, value=locator).click()

