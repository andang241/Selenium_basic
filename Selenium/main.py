from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_driver = "D:\Development\chromedriver_win32\chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get("https://www.python.org/")
events = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
list = events.text.split("\n")
dic = {}
for number in range(0, len(list)):
    if number % 2 == 0:
        dic[list[number]] = list[number + 1]
    else:
        continue
print(dic)
driver.quit()
