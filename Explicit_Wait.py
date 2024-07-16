from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait

chr_options = Options()
chr_options.add_experimental_option("detach",True)
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_121.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)
my_wait=WebDriverWait(driver,10)

driver.get("https://saucelabs.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-1xsl160']//a//button").click()

driver.switch_to.window(driver.window_handles[1])
click_google =my_wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Authenticate with Google']")))
click_google.click()

#driver.close()
#driver.quit()