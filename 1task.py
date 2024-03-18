
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import csv


import time
import random

url = "https://www.nseindia.com/"

options = webdriver.ChromeOptions()
options.add_argument("user-agent={hi=)}")
#options.add_argumentr=("--proxy-server=128.128.91.65:8000")
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service(r"C:\Users\89833\PycharmProjects\pythonProject\chrome\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get(url=url)
    time.sleep(random.uniform(1, 3))

    element = driver.find_element('xpath', '//a[@id="link_2"]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(random.uniform(2, 4))

    driver.find_element('link text', 'Pre-Open Market').click()
    time.sleep(random.uniform(3, 7))
    SYMBOL = driver.find_elements('xpath','//a[@class="symbol-word-break"]')
    Final_cost = driver.find_elements('xpath', '//td[@class="bold text-right"]')


    with open('itog.csv', 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Имя', 'Цена'])
        for symbol, cost in zip(SYMBOL, Final_cost):
            writer.writerow([symbol.text, cost.text])
    csvfile.close()

    driver.execute_script("window.scrollBy(0,50);")
    time.sleep(random.uniform(0.2,0.5))
    driver.execute_script("window.scrollBy(0,50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0,50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0,50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0, 50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0, 50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0, 50);")
    time.sleep(random.uniform(0.2, 0.5))

    driver.find_element('xpath', '//a[text()="TATAMOTORS"]').click()
    time.sleep(random.uniform(2,4))
    time.sleep(3)

    driver.execute_script("window.scrollBy(0,50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0,50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0,50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0,-50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0,-50);")
    time.sleep(random.uniform(0.2, 0.5))
    driver.execute_script("window.scrollBy(0,-50);")
    time.sleep(random.uniform(0.2, 0.5))

    element = driver.find_element('xpath', '//a[@id="link_4"]')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(random.uniform(1, 3))

    driver.find_element('link text', 'NEAPS Portal').click()
    time.sleep(random.uniform(5, 7))
finally:
    driver.close()
