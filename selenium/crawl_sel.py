from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import csv

options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
data = []

token_file = open('C:/Users/lenovo/Desktop/Programming/Python/web_scrapying/divar/tokens.txt', 'r', encoding='utf8')
tokens = token_file.read().split(",")
token_file.close()

for i in tokens:
    url = f"https://divar.ir/v/-/{i}"
    driver.get(url)
    time.sleep(1)

    try:

        metraj_element = driver.find_element(By.CSS_SELECTOR,
                                             value='.kt-group-row-item__value.kt-group-row-item--info-row:nth-child(1)')
        metraj = metraj_element.text
        sakht_element = driver.find_element(By.CSS_SELECTOR,
                                            value='.kt-group-row-item__value.kt-group-row-item--info-row:nth-child(2)')
        sakht = sakht_element.text
        rooms_element = driver.find_element(By.CSS_SELECTOR,
                                            value='.kt-group-row-item--info-row~ .kt-group-row-item--info-row+ .kt-group-row-item__value')
        rooms = rooms_element.text
        elevator_element = driver.find_element(By.CSS_SELECTOR, value='.kt-body--stable:nth-child(1)')
        elevator = elevator_element.text
        elevator = True if elevator == "آسانسور" else False
        time.sleep(1)
        parking_element = driver.find_element(By.CSS_SELECTOR, value='.kt-body--stable:nth-child(2)')
        parking = parking_element.text
        parking = True if parking == "پارکینگ" else False
        anbari_element = driver.find_element(By.CSS_SELECTOR, value='.kt-body--stable:nth-child(3)')
        anbari = anbari_element.text
        anbari = True if anbari == "انباری" else False
        price_element = driver.find_element(By.CSS_SELECTOR,
                                            value='.kt-unexpandable-row:nth-child(5) .kt-unexpandable-row__value')
        price = price_element.text
        address_element = driver.find_element(By.CSS_SELECTOR, value='.kt-page-title__subtitle--responsive-sized')
        address = address_element.text
        time.sleep(1)
    except NoSuchElementException as e:
        print(f"Error: {e}")
        continue
    data.append([metraj, sakht, rooms, elevator, parking, anbari, price, address])

driver.quit()

with open('divar_apartmens1.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['metraj', 'sakht', 'rooms', 'elevator', 'parking', 'anbari', 'price', 'address'])
    writer.writerows(data)

print("Data saved")
