from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_drive_path = "D:\Development\chromedriver_win32\chromedriver.exe"
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
chrome_service = Service(executable_path=chrome_drive_path)
drive = webdriver.Chrome(service=chrome_service, options=chrome_option)
drive.maximize_window()
drive.get("https://secure-retreat-92358.herokuapp.com/")
# editor_number = drive.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# print(editor_number.text)
# editor_number.click()

fname = drive.find_element(By.NAME, value='fName')
fname.send_keys("andang")
lname = drive.find_element(By.NAME, value='lName')
lname.send_keys("he")
email = drive.find_element(By.NAME, value='email')
email.send_keys("andang@gmail.com")

sign_button = drive.find_element(By.XPATH, value='/html/body/form/button')
sign_button.click()