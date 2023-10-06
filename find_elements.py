import pdb # -- this is the python debugger
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("http://demostore.supersqa.com/")
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "orderby").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/main/div[1]/form/select/option[5]").click()

time.sleep(5) # -- this will pause the execution of the script for 5 seconds


cart = driver.find_element(By.ID, "site-header-cart")
print(cart)
print(type(cart))
cart_txt = cart.text
print(cart_txt)

# driver.close() -- this will close the current tab
# driver.quit() -- this will close the browser

search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
search_field.send_keys("T-shirt")
# -- this will press the enter key
search_field.send_keys(Keys.ENTER)


# BY.CSS_SELECTOR
my_account = driver.find_element(By.CSS_SELECTOR, "#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9")
my_account.click()

# pdb.set_trace()  -- this will stop the execution of the script and open a python shell
