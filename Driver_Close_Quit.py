from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chr_options = Options()
chr_options.add_experimental_option("detach",True)
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_121.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)
driver.implicitly_wait(20)


driver.get("https://saucelabs.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-1xsl160']//a//button").click()

#driver.close()
driver.quit()
