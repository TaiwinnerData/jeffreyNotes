from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# chrome driver path: C:\Users\user\Desktop\chromedriver_win32\chromedriver.exe
# get web driver(Chrome) 
webdriver_path = r"C:\Users\user\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(webdriver_path)


try:
    # go to website 
    driver.get('https://www.browserstack.com/test-on-the-right-mobile-devices')

   
    # this website would ask you to accept cookies before you start to do something 
    # so click the "Acccept all" button
    gotit= driver.find_element(By.ID, 'accept-cookie-notification')
    gotit.click()

    
    # after click the "Accept all" button, click download csv button
    downloadcsv= driver.find_element(By.CLASS_NAME, 'icon-csv')
    downloadcsv.click()

    
    # add this line for web response
    time.sleep(5)    

    
    driver.close()
except Exception as ex:
     print("Invalid URL")
     print(ex)

