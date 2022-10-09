###  Import Module
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tanggal import thnskr, bulanangka, bulan, bsk, tanggalbesok, tanggallusa, skr

### File yang di upload dan narasi
folderNDF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/NDF/"+skr+"/")
narasi1 = ("Hallo #SobatBMKG")
narasi2 = ("Berikut admin bagikan Informasi Prakiraan Cuaca Tingkat Kecamatan Provinsi Papua berlaku mulai tanggal "+tanggalbesok+" pukul 09.00 WIT")
narasi = ("Hallo #SobatBMKG Berikut admin bagikan Informasi Prakiraan Cuaca Tingkat Kecamatan Provinsi Papua berlaku mulai tanggal "+tanggalbesok+" pukul 09.00 WIT")
image1 = folderNDF+"asmat.png\n"+folderNDF+"biak.png\n"+folderNDF+"bintang1.png\n"+folderNDF+"bintang2.png\n"+folderNDF+"boven.png\n"+folderNDF+"deiyai.png\n"+folderNDF+"dogiyai.png\n"+folderNDF+"intan.png\n"+folderNDF+"jayawijaya.png\n"+folderNDF+"jprkab.png\n"+folderNDF+"jprkota.png\n"+folderNDF+"keerom.png\n"+folderNDF+"lanny.png\n"+folderNDF+"mamberaya.png\n"+folderNDF+"mamteng.png\n"+folderNDF+"mappi.png"
image2 = folderNDF+"merauke.png\n"+folderNDF+"mimika.png\n"+folderNDF+"nabire.png\n"+folderNDF+"ndunga.png\n"+folderNDF+"paniai.png\n"+folderNDF+"puncak.png\n"+folderNDF+"sarmi.png\n"+folderNDF+"supiori.png\n"+folderNDF+"toli1.png\n"+folderNDF+"toli2.png\n"+folderNDF+"waropen.png\n"+folderNDF+"yahu1.png\n"+folderNDF+"yahu2.png\n"+folderNDF+"yahu3.png\n"+folderNDF+"yalimo.png\n"+folderNDF+"yapen.png"

## Setting Chrome Driver
import pathlib
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
chromeOptions.headless = True
driver = webdriver.Chrome(driverPath, options=chromeOptions)

#Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 6000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Info BMKG Papua", Keys.ENTER)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(narasi1)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(Keys.SHIFT, Keys.ENTER)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(narasi2, Keys.ENTER)
#time.sleep(60000)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(image1)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
time.sleep(5)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(image2)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()


##Telegram
import telegram
from telegram import InputMediaPhoto as imp
apiToken = '5663329448:AAFYtirH9HbrgcsJWPisd-blu-AL1jV0Aes'
chatID = '-38488324'
bot = telegram.Bot(token=apiToken)
bot.send_media_group(chat_id=chatID,media=[imp(open(folderNDF+"asmat.png", 'rb')), imp(open(folderNDF+"biak.png", 'rb')), imp(open(folderNDF+"bintang1.png", 'rb')), imp(open(folderNDF+"bintang2.png", 'rb')), imp(open(folderNDF+"boven.png", 'rb')), imp(open(folderNDF+"deiyai.png", 'rb')), imp(open(folderNDF+"dogiyai.png", 'rb')), imp(open(folderNDF+"intan.png", 'rb'))])
time.sleep(60)
bot.send_media_group(chat_id=chatID,media=[imp(open(folderNDF+"jayawijaya.png", 'rb')), imp(open(folderNDF+"jprkab.png", 'rb')), imp(open(folderNDF+"jprkota.png", 'rb')), imp(open(folderNDF+"keerom.png", 'rb')), imp(open(folderNDF+"lanny.png", 'rb')), imp(open(folderNDF+"mamberaya.png", 'rb')), imp(open(folderNDF+"mamteng.png", 'rb')), imp(open(folderNDF+"mappi.png", 'rb'))])
time.sleep(60)
bot.send_media_group(chat_id=chatID,media=[imp(open(folderNDF+"merauke.png", 'rb')), imp(open(folderNDF+"mimika.png", 'rb')), imp(open(folderNDF+"nabire.png", 'rb')), imp(open(folderNDF+"ndunga.png", 'rb')), imp(open(folderNDF+"paniai.png", 'rb')), imp(open(folderNDF+"puncak.png", 'rb')), imp(open(folderNDF+"sarmi.png", 'rb')), imp(open(folderNDF+"supiori.png", 'rb'))])
time.sleep(60)
bot.send_media_group(chat_id=chatID,media=[imp(open(folderNDF+"toli1.png", 'rb'), caption=narasi), imp(open(folderNDF+"toli2.png", 'rb')), imp(open(folderNDF+"waropen.png", 'rb')), imp(open(folderNDF+"yahu1.png", 'rb')), imp(open(folderNDF+"yahu2.png", 'rb')), imp(open(folderNDF+"yahu3.png", 'rb')), imp(open(folderNDF+"yalimo.png", 'rb')), imp(open(folderNDF+"yapen.png", 'rb'))])

time.sleep(60)
#driver.quit()