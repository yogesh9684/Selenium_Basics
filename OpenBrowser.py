from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


chr_options = Options()
chr_options.add_experimental_option("detach",True)
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_121.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)

driver.get("https://www.youtube.com")
driver.maximize_window()