from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
load_dotenv()
url=os.getenv("url")
mail=os.getenv("mail")
password=os.getenv("password")
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")# Create a folder for the Chrome Profile Selenium will use every time
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver=webdriver.Chrome(options=chrome_options)
driver.get(url=url)
# to click login button
wait=WebDriverWait(driver,5)
buttom=wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
buttom.click()
# to put inputs 
email_input=wait.until(EC.presence_of_element_located((By.ID,"email-input")))
password_input=wait.until(EC.presence_of_element_located((By.ID,"password-input")))
email_input.send_keys(mail)
password_input.send_keys(password)
# clicking subbmit button
submit_button=wait.until(EC.element_to_be_clickable((By.ID,"submit-button")))
submit_button.click()