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

driver.get("https://qavbox.github.io/demo/webtable/")
driver.maximize_window()

#To Print Table Rows
No_of_Rows=driver.find_elements(By.XPATH,"//table[@id='table02']//tr")
print("No of Rows",len(No_of_Rows))

#To Print Table Data
Table_data=driver.find_elements(By.XPATH,"//table[@id='table02']//tr//td")
for value in Table_data:
    print(value.text, end=" ")

#To Print Table Columns
# Table_Column = driver.find_elements(By.XPATH,"//table[@id='table02']//tr//th")
# print("No.of Column",len(Table_Column))
# for Value in Table_Column:
#     print(Value.text)

