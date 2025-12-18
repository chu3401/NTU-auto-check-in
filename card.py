from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import time
import random 
random1 = random.uniform(3, 5)
random2 = random.uniform(3, 5)
random3 = random.uniform(1.0, 2)

driver_path = r"your\path\chromedriver.exe"


service = Service(driver_path)


driver = webdriver.Chrome(service=service)


driver.get("")

time.sleep(3+random1)
username_input = driver.find_element(By.NAME, "user")  
password_input = driver.find_element(By.NAME, "pass")  
time.sleep(random2)
username_input.send_keys("xxxxxxxxxx")
password_input.send_keys("xxxxxxxxxx")    

login_button = driver.find_element(By.NAME, "Submit")  
login_button.click()  
time.sleep(3+random3)

sign_out_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "btSign")))
sign_out_button.click()

time.sleep(3)  

screenshot_path="./pic.png"
driver.save_screenshot(screenshot_path)
driver.quit()


