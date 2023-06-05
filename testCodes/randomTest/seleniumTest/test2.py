from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# get webdriver
webdriver_path = r"C:\Users\user\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(webdriver_path)


# start webdriver and go to website
url = "http://demo.automationtesting.in/FileDownload.html"
driver.get(url)
 

# Enter text
driver.find_element(By.ID, 'textbox').send_keys("Taiwinner")
 

# Generate Text File
driver.find_element(By.ID, 'createTxt').click()


# wait for website to create text file
time.sleep(3)

  
# Click on Download Button
driver.find_element(By.ID, 'link-to-download').click()


# wait for website download completed
time.sleep(5)


driver.close()
