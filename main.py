from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import random

x = 0
while x < 10:
    options = webdriver.EdgeOptions()
    options.add_experimental_option('detach', True)
    driver = webdriver.Edge(options=options)
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScb-vfM4PKTlDk9OmSvVMu-m9iH7vXV6UgsQvzbxRgRWSW0HQ/viewform')
    radio1 = driver.find_elements(By.CLASS_NAME, 'zwllIb')
    button = driver.find_elements(By.CLASS_NAME, 'uArJ5e')
    random_number = random.randint(0, 1)
    radio1[random_number].click()
    random_number = random.randint(2, 5)
    radio1[random_number].click()
    random_number = random.randint(6, 9)
    radio1[random_number].click()
    random_number = random.randint(10, 12)
    radio1[random_number].click()
    time.sleep(1)
    button[0].click()
    radio2 = driver.find_elements(By.CLASS_NAME, 'zwllIb')
    button2 = driver.find_elements(By.CLASS_NAME, 'uArJ5e')
    random_number = random.randint(0, 4)
    radio2[random_number].click()
    random_number = random.randint(5, 9)
    radio2[random_number].click()
    random_number = random.randint(10, 14)
    radio2[random_number].click()
    time.sleep(1)
    button2[1].click()
    radio_select = driver.find_elements(By.CLASS_NAME, 'd7L4fc')
    time.sleep(1)
    element = driver.find_elements(By.CLASS_NAME, 'Od2TWd')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div/div[1]/div[2]')
    y = 0
    for i in range(1, 105):
        temp = y + 6
        random_number = random.randint(y, temp)
        y = y + 7
        class_names = element[random_number].get_attribute('class')
        if 'RDPZE' in class_names:
            continue
        element[random_number].click()
    submit_button.click()
    time.sleep(1)
    driver.close()
    x = x + 1








