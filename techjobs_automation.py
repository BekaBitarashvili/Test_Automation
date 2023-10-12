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
driver.get("https://techjobs.onrender.com/home")
driver.maximize_window()

# try login
driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[1]/input").send_keys("test")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[2]/input").send_keys("test")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[3]/input").click()

# try register
driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[4]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[1]/input").send_keys("automation")
driver.find_element(By.XPATH, "//html/body/div/div/div/div/div/div/div/form/div[2]/input").send_keys("auto@posta.ge")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[3]/input").send_keys("bitara123")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[4]/input").send_keys("bitara123")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[5]/input").click()

if driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/h2").text == "500 ERROR":
    print("PASS")


# try real login
driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[1]/input").send_keys("auto@posta.ge")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[2]/input").send_keys("bitara123")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[3]/input").click()

# add new job
driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[3]/a").click()
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[1]/input").send_keys("automation")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[2]/textarea").send_keys("automation")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[3]/input").send_keys("automation")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[4]/input").send_keys("automation")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[5]/textarea").send_keys("automation")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[6]/textarea").send_keys("automation")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[7]/textarea").send_keys("automation")
driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div/div/form/div[8]/input").click()