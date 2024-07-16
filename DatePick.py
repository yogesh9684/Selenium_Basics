from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#To keep session Open
chr_options = Options()
chr_options.add_experimental_option("detach",True)

#Executable Path
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver_123.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)

driver.get("https://designsystem.digital.gov/components/date-picker/")
driver.maximize_window()
driver.implicitly_wait(10)

#driver.find_element(By.XPATH,"//button[@class='usa-date-picker__button']").click()

Exp_Day ="12"
Exp_Month ="December"
Exp_Year ="2012"
# Date_Send = driver.find_element(By.XPATH,"//input[@id='appointment-date']")
# Date_Send.send_keys("29/07/1992")

driver.find_element(By.XPATH,"//button[@class='usa-date-picker__button']").click()
#driver.find_element(By.XPATH, "//button[@class='usa-date-picker__calendar__month-selection']").click()

#Main Section

while True:
    driver.find_element(By.XPATH, "//button[@class='usa-date-picker__calendar__previous-month']").click()
    current_month_selected = driver.find_element(By.XPATH,"//button[@class='usa-date-picker__calendar__month-selection']").text
    #driver.find_element(By.XPATH,"//button[@class='usa-date-picker__calendar__previous-year']").click()
    current_year_selected = driver.find_element(By.XPATH,"//button[@class='usa-date-picker__calendar__year-selection']").text
    if current_year_selected == Exp_Year and current_month_selected == Exp_Month:
                break
All_Days = driver.find_elements(By.XPATH,"//table[@class='usa-date-picker__calendar__table']//tbody//tr//td")
for day in All_Days:
    if day.text == Exp_Day:
        day.click()
        break


