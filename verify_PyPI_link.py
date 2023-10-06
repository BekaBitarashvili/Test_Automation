import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://python.org/")
title = driver.title
expected_title = "Welcome to Python.org"

if title != expected_title:
    raise Exception("The title of the page is not the expected one")


pypi_link = driver.find_element(By.XPATH, "/html/body/div/div[2]/nav/ul/li[4]/a")
pypi_link.click()

url = driver.current_url
expected_url = "https://pypi.org/"
assert url == expected_url, f"The url is not the expected one. Expected: {expected_url}. Actual: {url}"
print("PASS")