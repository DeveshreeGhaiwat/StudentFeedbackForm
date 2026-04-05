from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open your local feedback form
driver.get("file:///Users/deveshreeghaiwat/Documents/StudentFeedbackForm/index.html")

print("🟡 Please fill the form manually in the browser...")

# Wait for user to fill form manually
input("👉 Press ENTER after filling the form and clicking submit...")

# Optional: Validation check
if "thank" in driver.page_source.lower() or "submitted" in driver.page_source.lower():
    print("✅ Form submitted successfully")
else:
    print("⚠️ Submission not confirmed (check manually)")

# Wait before closing (optional)
time.sleep(2)

driver.quit()
