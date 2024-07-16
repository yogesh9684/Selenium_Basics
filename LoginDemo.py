from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import Excel_Utility

chr_options = Options()
chr_options.add_experimental_option("detach",True)
serv_object = Service(executable_path=r'C:\\browser_drivers\\chromedriver.exe')
driver=webdriver.Chrome(service=serv_object,options=chr_options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(1)

file = "C:\\Users\\YOGESH\\Documents\\DataDrivenTest.xlsx"

rows = Excel_Utility.get_row_count(file,"Sheet1")

for r in range(2,rows+1):
    username=Excel_Utility.read_data(file,"Sheet1",r,1)
    password=Excel_Utility.read_data(file,"Sheet1",r,2)

    try:
        username1=driver.find_element(By.XPATH,"//input[@name='username']").send_keys(username)
        password1=driver.find_element(By.XPATH,"//input[@name='password']").send_keys(password)

        #clicking on submit button
        Submit =driver.find_element(By.XPATH,"//button[@type='submit']").click()

        #Check if Dashboard Label is displayed
        dashboard = driver.find_element(By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']//h6").text
        Actual_dashboard= "Dashboard"

        if dashboard == Actual_dashboard:
            Excel_Utility.write_data(file,"Sheet1",r,4,"Passed")
            Excel_Utility.fill_green(file,"Sheet1",r,4)

            # clicking on Logout Button
            driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()
            click_logout = driver.find_element(By.XPATH, "//ul[@class='oxd-dropdown-menu']//li[4]//a").click()

        else:
            Excel_Utility.write_data(file, "Sheet1", r, 4, "Failed")
            Excel_Utility.fill_red(file, "Sheet1", r, 4)

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
        Excel_Utility.write_data(file, "Sheet1", r, 4, "Failed")
        Excel_Utility.fill_red(file, "Sheet1", r, 4)




