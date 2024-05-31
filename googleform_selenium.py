from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()  # Make sure chromedriver is installed and in your PATH

# Open the Google Form
driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

time.sleep(5)

# Full Name
full_name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
full_name_field.send_keys('Aman Agarwal')

# Contact
contact_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
contact_field.send_keys('9711937828')

# email
email_id = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_id.send_keys('amannagarwal13@gmail.com')

# Contact
address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
address.send_keys('8079, B-11, Vasant Kunj')

# Contact
pincode = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
pincode.send_keys('110070')

# Birthdate
birthdate_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
birthdate_field.send_keys('12/13/2001')

# Contact
gender = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
gender.send_keys('Male')

# Contact
code = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
code.send_keys('GNFPYC')

# Submit the form
#submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()

# Wait for the confirmation page to load
time.sleep(5)

# Take a screenshot of the confirmation page
screenshot_path = 'confirmation_screenshot.png'
driver.save_screenshot(screenshot_path)

# Close the driver
driver.quit()
