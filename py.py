###  Import Module
import os
import time
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tanggal import thnskr, bulanangka, bulan, skr, tanggalsekarang, hariini
import pyautogui

## Setting Chrome Driver
import pathlib
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(driverPath, options=chromeOptions)

driver.get("https://www.instagram.com/")

time.sleep(5)
upload=driver.find_element_by_xpath('//div[@class="QBdPU "]')
upload.click()
time.sleep(2)
img_upload=driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]').click()
time.sleep(2)
path = "D:\Pictures\ph.png" # your imagepath
pyautogui.write(path) 
time.sleep(2)
pyautogui.press('enter')