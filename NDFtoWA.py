###  Import Module
import os
import time
import urllib.request
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tanggal import thnskr, bulanangka, bulan, bsk, tanggalbesok, tanggallusa

### File yang di upload dan narasi
folderNDF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/NDF/"+bsk+"/")
asmat = os.path.realpath(folderNDF+"asmat.png")
biak = os.path.realpath(folderNDF+"biak.png")
bintang1 = os.path.realpath(folderNDF+"bintang1.png")
bintang2 = os.path.realpath(folderNDF+"bintang2.png")
boven = os.path.realpath(folderNDF+"boven.png")
deiyai = os.path.realpath(folderNDF+"deiyai.png")
dogiyai = os.path.realpath(folderNDF+"dogiyai.png")
intan = os.path.realpath(folderNDF+"intan.png")
jayawijaya = os.path.realpath(folderNDF+"jayawijaya.png")
jprkab = os.path.realpath(folderNDF+"jprkab.png")
jprkota = os.path.realpath(folderNDF+"jprkota.png")
keerom = os.path.realpath(folderNDF+"keerom.png")
lanny = os.path.realpath(folderNDF+"lanny.png")
mamberaya = os.path.realpath(folderNDF+"mamberaya.png")
mamteng = os.path.realpath(folderNDF+"mamteng.png")
mappi = os.path.realpath(folderNDF+"mappi.png")
merauke = os.path.realpath(folderNDF+"merauke.png")
mimika = os.path.realpath(folderNDF+"mimika.png")
nabire = os.path.realpath(folderNDF+"nabire.png")
nduga = os.path.realpath(folderNDF+"ndunga.png")
paniai = os.path.realpath(folderNDF+"paniai.png")
puncak = os.path.realpath(folderNDF+"puncak.png")
sarmi = os.path.realpath(folderNDF+"sarmi.png")
supiori = os.path.realpath(folderNDF+"supiori.png")
toli1 = os.path.realpath(folderNDF+"toli1.png")
toli2 = os.path.realpath(folderNDF+"toli2.png")
waropen = os.path.realpath(folderNDF+"waropen.png")
yahu1 = os.path.realpath(folderNDF+"yahu1.png")
yahu2 = os.path.realpath(folderNDF+"yahu2.png")
yahu3 = os.path.realpath(folderNDF+"yahu3.png")
yalimo = os.path.realpath(folderNDF+"yalimo.png")
yapen = os.path.realpath(folderNDF+"yapen.png")

narasi1 = ("Hallo #SobatBMKG")
narasi2 = ("Berikut admin bagikan Informasi Prakiraan Cuaca Tingkat Kecamatan Provinsi Papua berlaku mulai tanggal "+tanggalbesok+" pukul 09.00 WIT")

## Setting Chrome Driver
currentPath = __file__.split("Whatsapp.py")[0] 
driverPath = 'C:/Ripcy/Script_1/Ripcy/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(driverPath, options=chromeOptions)

#Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 6000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Arif Ripcy", Keys.ENTER)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(narasi1)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(Keys.SHIFT, Keys.ENTER)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(narasi2, Keys.ENTER)
#time.sleep(60000)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(asmat)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#app > div > div > div._3ArsE > div.ldL67._3sh5K > span > div > span > div > div > div.g0rxnol2.thghmljt.p357zi0d.ggj6brxn.f8m0rgwh.gfz4du6o.r7fjleex.bs7a17vp > div > div._1HI4Y > div.p357zi0d.ktfrpxia.nu7pwgvd.ac2vgrno.sap93d0t.r15c9g6i._1vAZI > button'))).send_keys(biak)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(bintang1)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(bintang2)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(boven)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(deiyai)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(dogiyai)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(intan)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(jayawijaya)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(jprkota)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(jprkab)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(lanny)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(mamberaya)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(mamteng)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(mappi)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(merauke)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(mimika)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(nabire)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(nduga)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(paniai)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(puncak)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(sarmi)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(supiori)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(toli1)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(toli2)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(waropen)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(yahu1)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(yahu2)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(yahu3)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(yalimo)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(yapen)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
driver.quit()
