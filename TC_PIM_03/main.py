from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DeleteExistingEmployee:

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

   def deleteEmployee(self):
       locator.WebLocators().click(self.driver, locator.WebLocators().PIMLocator)
       element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span')
       self.driver.execute_script("arguments[0].scrollIntoView();", element)
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


obj = DeleteExistingEmployee()
obj.login()
obj.deleteEmployee()
