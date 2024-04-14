from Locators import locator
from Data import data

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Explicit wait
from selenium.webdriver.support.ui import WebDriverWait
import pytest

class Test:

   @pytest.fixture
   def boot(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
       yield
       self.driver.quit()


   @pytest.mark.html
   def testTitle(self, boot):
       self.driver.get(data.WebData().url)
       assert self.driver.title == data.WebData().loginPageTitle
       print("SUCCESS: Web Title Verified")


   @pytest.mark.html
   def testLogin(self, boot):
       self.driver.get(data.WebData().url)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
       assert self.driver.current_url == data.WebData().dashboardURL
       print(f"SUCCESS : Logged in with {data.WebData().username} and the password is {data.WebData().password}")


