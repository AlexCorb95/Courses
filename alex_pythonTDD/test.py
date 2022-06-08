from pprint import pprint

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def max_page(driver):
    pager = driver.find_element(by=By.CLASS_NAME, value='pager')
    all_pages = pager.find_elements(by=By.CLASS_NAME, value="fleft")
    last_page = all_pages[len(all_pages) - 1]
    last_page_link = last_page.find_element(by=By.TAG_NAME, value="a")
    last_page_link_child = last_page_link.find_element(by=By.TAG_NAME, value="span")
    max_page = last_page_link_child.get_attribute("innerText")
    return int(max_page)


def parse_result(result):
    try:
        details_link = result.find_element(by=By.CLASS_NAME, value='detailsLink')
        href = details_link.get_attribute('href')

        return {"link": href}
    except NoSuchElementException:
        print("No details")
        return None


all_ads = []
driver = webdriver.Chrome()
driver.get("https://www.olx.ro/")
elem = driver.find_element(by=By.NAME, value="q")
elem.clear()
elem.send_keys("logitech g29")
elem.send_keys(Keys.RETURN)
last_page = max_page(driver)
url = driver.current_url

for page in range(1, last_page + 1):
    driver.get(url + f"?page={page}")
    driver.implicitly_wait(3)
    offers_tabel = driver.find_element(by=By.ID, value="offers_table")
    wrap_list = offers_tabel.find_elements(by=By.CLASS_NAME, value="wrap")
    for result in wrap_list:
        ad = parse_result(result)
        if ad is not None:
            all_ads.append(ad)

pprint(all_ads)
