from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait

class  AddNewEmployee:

   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       self.wait = WebDriverWait(self.driver, 10)

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()

   def quit(self):
       self.driver.quit()

   def login(self):
       try:
           self.boot()
           locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
           locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
           locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)

           if self.driver.current_url == data.WebData().dashboardURL:
               print("Successfully LoggedIn")
       except NoSuchElementException as e:
           print("Error!")

   def addEmployee(self):
       locator.WebLocators().click(self.driver, locator.WebLocators().PIMLocator)
       locator.WebLocators().click(self.driver, locator.WebLocators().addLocator)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().firstNameLocator, data.WebData().firstName)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().lastNameLocator, data.WebData().lastName)
       locator.WebLocators().click(self.driver, locator.WebLocators().saveLocator)
       print("Employee added successfully!")

   def addPersonalDetails(self):
       locator.WebLocators().enterText(self.driver, locator.WebLocators().middleNameLocator, data.WebData().middleName)
       locator.WebLocators().text(self.driver, locator.WebLocators().IDLocator, data.WebData().otherID)
       locator.WebLocators().text(self.driver, locator.WebLocators().licenseLocator, data.WebData().licenseNo)
       locator.WebLocators().text(self.driver, locator.WebLocators().expiryDateLocator, data.WebData().expiryDate)
       locator.WebLocators().text(self.driver, locator.WebLocators().dobLocator, data.WebData().DOB)
       locator.WebLocators().click(self.driver, locator.WebLocators().SaveLocator)
       self.quit()


obj = AddNewEmployee()
obj.login()
obj.addEmployee()
obj.addPersonalDetails()
