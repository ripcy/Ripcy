###  Import Module
import os, os.path, time, urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tanggal import *

### File yang di upload dan narasi
try:
    os.makedirs("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF")
except FileExistsError:
    # directory already exists
    pass
folderIBF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF/")
src1 = "https://web.meteo.bmkg.go.id//media/data/bmkg/ibfnew/34_papua_24.png"
if os.path.exists(folderIBF+bsk+".png"):
    pass
else:
    urllib.request.urlretrieve(src1, folderIBF+bsk+".png")

src1 = "https://web.meteo.bmkg.go.id//media/data/bmkg/ibfnew/34_papua_48.png"
if os.path.exists(folderIBF+bsk2+".png"):
    pass
else:
    urllib.request.urlretrieve(src1, folderIBF+bsk2+".png")
image = folderIBF+bsk+".png\n"+folderIBF+bsk2+".png"
narasi = ("Informasi Prakiraan Cuaca Berbasis Dampak wilayah Provinsi Papua berlaku 2 hari kedepan, tanggal "+tanggalbesok+" pukul 09.00 WIT - "+tanggallusa2+" pukul 09.00 WIT. Informasi Prakiraan Cuaca Berbasis Dampak hingga level kecamatan dapat diakses pada : http://signature.bmkg.go.id/")

### Setting Driver
import pathlib
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeService = Service(driverPath)
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
chromeOptions.headless = True
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(service=chromeService, options=chromeOptions)

## Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Info BMKG Papua", Keys.ENTER)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(image)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'))).send_keys(narasi)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
time.sleep(10)

##Telegram
import telegram
from telegram import InputMediaPhoto as imp
apiToken = '5663329448:AAFYtirH9HbrgcsJWPisd-blu-AL1jV0Aes'
chatID = '-38488324'
bot = telegram.Bot(token=apiToken)
bot.send_media_group(chat_id=chatID,media=[imp(open(folderIBF+bsk+".png", 'rb'), caption=narasi), imp(open(folderIBF+bsk2+".png", 'rb'))])


driver.quit()
