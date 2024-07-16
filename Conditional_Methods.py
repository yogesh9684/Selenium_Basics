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

driver.get("https://api.cogmento.com/register/?lang=en-GB")
driver.maximize_window()

element = driver.find_element(By.XPATH,"//input[@id='terms']")
element.click()
print(element.is_selected())
element.click()
print(element.is_selected())



