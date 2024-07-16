import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException


#To keep session Open
chr_options = Options()
chr_options.add_experimental_option("detach",True)

#Executable Path
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_123.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)

driver.get("https://www.udemy.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#driver.save_screenshot("E:\\Selenium\\Screenshots\\test.png")

#driver.get_screenshot_as_file("E:\\Selenium\\Screenshots\\test1.png")

#to take the screenshots of specific path only
Image_Logo=driver.find_element(By.XPATH,"//a[@id='popper-trigger--16']")
Image_Logo.screenshot("E:\\Selenium\\Screenshots\\test2.png")
driver.close()
