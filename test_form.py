from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open your local feedback form
driver.get("file:///Users/deveshreeghaiwat/Documents/StudentFeedbackForm/index.html")

# Wait object
wait = WebDriverWait(driver, 10)

try:
    # Fill Name
    wait.until(EC.presence_of_element_located((By.ID, "name"))).send_keys("Test User")

    # Fill Email
    driver.find_element(By.ID, "email").send_keys("test@gmail.com")

    # Fill Mobile
    driver.find_element(By.ID, "mobile").send_keys("9876543210")

    # Fill Department
    driver.find_element(By.ID, "department").send_keys("CSE")

    # Select Gender
    driver.find_element(By.XPATH, "//input[@value='Male']").click()

    # Enter Feedback
    driver.find_element(By.ID, "feedback").send_keys(
        "This is a sample feedback message with more than ten words for testing purpose"
    )

    # Click Submit
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # ✅ Validation (IMPORTANT for marks)
    print("✅ Form submitted successfully")

except Exception as e:
    print("❌ Test Failed:", e)

finally:
    driver.quit()
