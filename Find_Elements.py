from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)

serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_121.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)


driver.get("https://saucelabs.com/")
driver.maximize_window()

extralinks =driver.find_elements(By.XPATH,"//div[@class='MuiStack-root css-j7qwjs']/div")
print("Links present in the Websites are",len(extralinks))
for links in extralinks:
    print(links.text)

