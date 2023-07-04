from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

list_price = []
list_ids = []


def get_price(drive_par, value, list_price_check):
    result = drive_par.find_element(By.CSS_SELECTOR, value)
    result = result.text.split("-")
    result[1] = result[1].strip()
    if "," in result[1]:
        result[1] = result[1].replace(",", "")
    list_price_check.append(result[1])


chrome_drive_path = "D:\Development\chromedriver_win32\chromedriver.exe"
chrome_option = Options()
chrome_service = Service(executable_path=chrome_drive_path)
chrome_option.add_experimental_option("detach", True)
drive = webdriver.Chrome(options=chrome_option, service=chrome_service)
drive.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = drive.find_element(By.ID, value="cookie")
money = drive.find_element(By.ID, value="money")

buy_elements = drive.find_elements(By.CSS_SELECTOR, '#store [id^="buy"]')
for element in buy_elements:
    element_id = element.get_attribute('id')
    list_ids.append(element_id)

list_ids.pop()


def upgrade_price(driver, list_price_check):
    list_price.clear()
    for object_id in list_ids:
        if " " in object_id:
            object_id = object_id.replace(" ", "\\ ")
            print(object_id)
        get_price(drive_par=driver, value=f"#{object_id} b", list_price_check=list_price_check)


time_check = time.time() + 5
time_out = time.time() + 60 * 5
is_continue = True
while is_continue:
    cookie.click()
    if time_check <= time.time():
        upgrade_price(driver=drive, list_price_check=list_price)
        for number in range(len(list_price) - 1, -1, -1):
            if float(money.text) >= float(list_price[number]):
                click_element = drive.find_element(By.ID, value=list_ids[number])
                click_element.click()
                break
        time_check += 10
    if time_out <= time.time():
        seconds = drive.find_element(By.ID, value="cps")
        print(seconds.text)
        drive.quit()
        is_continue = False
