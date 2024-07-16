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

driver.get("https://www.ibm.com/support/pages/node/6347580")
driver.maximize_window()
driver.implicitly_wait(10)

#to accept the cookies
driver.find_element(By.ID,"truste-consent-button").click()
time.sleep(3)

#to click on country Dropdown
driver.find_element(By.ID,"select2-language-container").click()
time.sleep(3)
driver.refresh()
#select the vailable Language

try:
    select_language = driver.find_elements(By.XPATH,"//select[@id='language']//option")
    for language in select_language:
        language = driver.find_element(By.XPATH, f"//select[@id='language']//option[text()='{language.text}']")
        if language.text == "Français - French":
            language.click()
except StaleElementReferenceException:
            # Handle the exception here, such as retrying or refreshing the page
        pass
finally:
        driver.quit()




















