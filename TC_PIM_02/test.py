from Locators import locator
from Data import data

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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


   @pytest.mark.html
   def testEditEmployee(self, boot):
       self.driver.get(data.WebData().url)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonLocator)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().click(self.driver, locator.WebLocators().PIMLocator)
       self.wait = WebDriverWait(self.driver, 10)
       element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span')
       self.wait = WebDriverWait(self.driver, 10)
       self.driver.execute_script("arguments[0].scrollIntoView();", element)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().click(self.driver, locator.WebLocators().clickLocator)
       self.wait = WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().firstNameLocator, data.WebData().firstName)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().middleNameLocator, data.WebData().middleName)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().lastNameLocator, data.WebData().lastName)
       locator.WebLocators().text(self.driver, locator.WebLocators().IDLocator, data.WebData().otherID)
       locator.WebLocators().text(self.driver, locator.WebLocators().licenseLocator, data.WebData().licenseNo)
       locator.WebLocators().text(self.driver, locator.WebLocators().expiryDateLocator, data.WebData().expiryDate)
       locator.WebLocators().text(self.driver, locator.WebLocators().dobLocator, data.WebData().DOB)
       locator.WebLocators().click(self.driver, locator.WebLocators().SaveLocator)



