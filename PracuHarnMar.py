###  Import Module
import os, os.path, time, urllib.request
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tanggal import thnskr, bulanangka, bulan, skr, tanggalbesok, tanggallusa, bsk, kmrn

### File yang di upload dan narasi
folderNDF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/NDF/"+skr+"/")
folderMar = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/MARITIM/")
allimage = folderNDF+"kabupaten.png \n" +folderMar+kmrn+".png"
image1 = folderNDF+"kabupaten.png"
image2 = folderMar+kmrn+".png"
narasi = ("Informasi prakiraan cuaca Kabupaten Provinsi Papua serta prakiraan cuaca pelayaran dan tinggi gelombang Perairan Papua - Papua Barat, "+tanggalbesok+" berlaku 24 jam mulai pukul 09.00 WIT")

### Setting Driver
import pathlib
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(driverPath, options=chromeOptions)
'''
## Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Arif", Keys.ENTER)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(narasi, Keys.ENTER)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(allimage)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
time.sleep(10)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
'''
driver.get("https://www.instagram.com/")
time.sleep(5000)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CLASS_NAME, '_ab6-'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]'))).click()

'''
## Telegram
import requests
apiToken = '5663329448:AAFYtirH9HbrgcsJWPisd-blu-AL1jV0Aes'
chatID = '40071216'
url = f'https://api.telegram.org/bot{apiToken}/sendPhoto?chat_id={chatID}'

response = requests.post(url, data={'caption': narasi}, files={'photo': open(image1, 'rb')})
'''