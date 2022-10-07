###  Import Module
import os, os.path, time, urllib.request, pyautogui
import autoit
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tanggal import thnskr, bulanangka, bulan, bsk, tanggalbesok, tanggallusa

### File yang di upload dan narasi
try:
    os.makedirs("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF")
except FileExistsError:
    # directory already exists
    pass
folderIBF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF/")
src = "https://web.meteo.bmkg.go.id//media/data/bmkg/ibfnew/34_papua_24.png"
if os.path.exists(folderIBF+bsk+".png"):
    pass
else:
    urllib.request.urlretrieve(src, folderIBF+bsk+".png")
image = folderIBF+bsk+".png"
narasi = ("Informasi Prakiraan Cuaca Berbasis Dampak wilayah Provinsi Papua berlaku "+tanggalbesok+" pukul 09.00 WIT - "+tanggallusa+" pukul 09.00 WIT Informasi lebih lengkap dapat diakses pada : http://signature.bmkg.go.id/")

### Setting Driver
import pathlib
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeService = Service(driverPath)
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(service=chromeService, options=chromeOptions)
'''
## Facebook
driver.get("https://www.facebook.com/")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xkjl1po > .x1lliihq'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x1a2a7pz > .x16tdsg8'))).send_keys(narasi)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x12mruv9:nth-child(2) .x1b0d499:nth-child(1)'))).click()
photo_element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
photo_element.send_keys(image)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xtk6v10 > .x1lliihq'))).click()

'''

driver.get('https://www.instagram.com/')
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_acub .\_ab6-'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//input[@accept='image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime']"))).send_keys(image)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_ab8w:nth-child(1) > .\_ab8w .\_abfz .\_ab6-'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_acan:nth-child(1) > .\_ab8w > .\_ab8w > .\_aacl'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_ab99 > .\_acan'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_ab99 > .\_acan'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_aaeg'))).send_keys(narasi)
post = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Share']"))).click()

time.sleep(600)
#
#pyautogui.write(video)

#pyautogui.hotkey('enter')
#WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))).send_keys(video)
#pyautogui.write(video)
#pyautogui.press('enter')
