from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.

# myapp/views.py

from django.core.mail import EmailMessage
from django.http import HttpResponse
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fill_form_and_send_email(request):
    # Run the Selenium script to fill the form
    fill_google_form()

    # Send notification email
    send_email_with_screenshot(request)

    return HttpResponse("Form filled and email sent successfully.")

def fill_google_form():
    # Set up the WebDriver
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
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    # Wait for the confirmation page to load
    time.sleep(5)

    # Take a screenshot of the confirmation page
    screenshot_path = 'confirmation_screenshot.png'
    driver.save_screenshot(screenshot_path)

    # Close the driver
    driver.quit()

def send_email_with_screenshot(request):
    email = EmailMessage(
        subject='Python (Selenium) Assignment - Aman Agarwal',
        body=(
            'Please find the attached screenshot of the Google Form submission confirmation page and pdf containing the methodology. This email has been entirely sent using Django automation and please note that the selenium script has been integrated in django application itself and I have attached it seperately also in the github repository under the name googleform_selenium. KINDLY IGNORE THE PREVIOUS EMAIL \n\n'
            'GitHub Link: https://github.com/amanagarwal13/Medius_Technologies\n\n'
            'Thanks and Regards,\n'
            'Aman Agarwal,\n'
            '9711937828'
        ),
        to=['tech@themedius.ai'],
        cc=['HR@themedius.ai','aman.agarwal7221@gmail.com']
    )

    # Define the paths to the files to be attached
    screenshot_path = os.path.join('confirmation_screenshot.png')
    pdf_path = os.path.join('AUTOMATING GOOGLE FORM SUBMISSION.pdf')  # Replace 'methodology.pdf' with the actual path to your PDF file

    # Attach the files to the email
    email.attach_file(screenshot_path)
    email.attach_file(pdf_path)

    email.send()

    return HttpResponse('Email sent successfully.')