from Locators import locator
from Data import data

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
   def testdeleteEmployee(self, boot):
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
       button = self.driver.find_element(By.XPATH, "//button[@class='oxd-icon-button oxd-table-cell-action-space']")
       # Wait for the overlay to disappear
       wait = WebDriverWait(self.driver, 10)
       wait.until(
           EC.invisibility_of_element_located((By.XPATH, "//div[@class='oxd-dialog-container-default--inner']")))
       # Click the button
       button.click()
       alert_dialogue = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.CLASS_NAME, "oxd-dialog-sheet"))
       )

       try:
           # Find the "Yes, Delete" button within the alert dialogue
           yes_button = WebDriverWait(alert_dialogue, 10).until(
               EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Yes, Delete')]"))
           )
           # Click the "Yes, Delete" button
           yes_button.click()
           print('Success:Existing employee is deleted')

       except Exception as e:
           print("Error:", e)




