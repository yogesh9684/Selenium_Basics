import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(10)

create_page_link=driver.find_element(By.LINK_TEXT,"Create a Page")

#to open the page in new window
click=Keys.CONTROL + Keys.ENTER
create_page_link.send_keys(click)

#driver.switch_to.window(driver.window_handles[1])


driver.switch_to.new_window('window')
driver.get("https://www.amazon.in")