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
search_field_id = 'id-search-field'
search_field = driver.find_element(By.ID, search_field_id)
search_field.send_keys("testing")

go_btn_id = 'submit'
go_btn = driver.find_element(By.ID, go_btn_id)
go_btn.click()