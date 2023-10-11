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

driver.implicitly_wait(5)
driver.get("http://demostore.supersqa.com/")

all_products = driver.find_elements(By.CLASS_NAME, "product-type-simple")
print(len(all_products))

one_price_product = []
for product in all_products:
    price_elm = product.find_element(By.CSS_SELECTOR, "span.amount").text

    name_elm = product.find_element(By.CLASS_NAME, "woocommerce-loop-product__title").text
    print(name_elm, price_elm)

    one_price_product.append({"name": name_elm, "price": price_elm})
print(len(one_price_product))
print(one_price_product)