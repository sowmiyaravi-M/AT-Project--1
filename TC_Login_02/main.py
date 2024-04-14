from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage:

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
           print("Invalid credentials")
       finally:
           self.quit()


obj = LoginPage()
obj.login()
