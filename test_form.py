from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("file:///Users/deveshreeghaiwat/Documents/StudentFeedbackForm/index.html")
driver.maximize_window()

driver.find_element(By.ID, "name").send_keys("Test User")
driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "mobile").send_keys("9876543210")

driver.find_element(By.ID, "department").send_keys("CSE")
driver.find_element(By.XPATH, "//input[@value='Male']").click()

driver.find_element(By.ID, "feedback").send_keys(
    "This is a sample feedback message with more than ten words for testing purpose"
)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(2)
driver.quit()
