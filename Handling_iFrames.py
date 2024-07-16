from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

#To keep session Open
chr_options = Options()
chr_options.add_experimental_option("detach",True)

#Executable Path
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_123.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

#Switching iFrame
driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys('Test12345')

#To come Out from the Iframe
driver.switch_to.default_content()

