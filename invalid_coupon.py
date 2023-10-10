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

driver.get("http://demostore.supersqa.com/")  # -- this will open the browser and navigate to the url
driver.maximize_window()  # -- this will maximize the browser window
driver.implicitly_wait(10)  # -- this will wait for 10 seconds for the element to be present before throwing an
driver.find_element(By.XPATH,
                    "/html/body/div[2]/div/div/div[2]/main/ul/li[3]/a[2]").click()  # -- this will click on the "Add
# to cart" button
driver.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div/nav/div[1]/ul/li[2]/a").click()
time.sleep(3) # -- this will pause the execution of the script for 3 seconds
driver.refresh() # -- this will refresh the page

driver.find_element(By.ID, "coupon_code").send_keys("123")
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/main/article/div/div/form/table/tbody/tr["
                              "2]/td/div/button").click()

check_flash_msg = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/main/article/div/div/div[1]"
                                                "/ul/li").text

if check_flash_msg == "Coupon '123' does not exist!":
    print("PASS")
