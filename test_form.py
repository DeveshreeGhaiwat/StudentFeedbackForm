from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("file:///Users/deveshreeghaiwat/Documents/StudentFeedbackForm/index.html")

print("🟡 Please fill the form manually in the browser...")

# Wait instead of input (IMPORTANT for Jenkins)
time.sleep(15)

# Validation
if "thank" in driver.page_source.lower() or "submitted" in driver.page_source.lower():
    print("✅ Form submitted successfully")
else:
    print("⚠️ Submission not confirmed")

driver.quit()
