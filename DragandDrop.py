from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#To keep session Open
chr_options = Options()
chr_options.add_experimental_option("detach",True)

#Executable Path
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_123.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

source=driver.find_element(By.ID,"draggable")
destination=driver.find_element(By.ID,"droppable")

act = ActionChains(driver)
act.drag_and_drop(source,destination).perform()
print("Element Dropped Successfully")