###  Import Module
import os, os.path, time
from selenium import webdriver
from telegram import Bot, InputMediaPhoto as imp
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from tanggal import thnskr, bulanangka, bulan, skr, tanggalbesok, tanggallusa, bsk, kmrn

### File yang di upload dan narasi
folderNDF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/NDF/"+skr+"/")
folderMar = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/MARITIM/")
allimage = folderNDF+"kabupaten.png \n"# +folderMar+bsk+".png"
narasi = ("Informasi prakiraan cuaca Kabupaten Provinsi Papua serta prakiraan cuaca pelayaran dan tinggi gelombang Perairan Papua - Papua Barat, "+tanggalbesok+" berlaku 24 jam mulai pukul 09.00 WIT")

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

## Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Info BMKG Papua", Keys.ENTER)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(narasi, Keys.ENTER)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(allimage)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
time.sleep(5)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])

## Facebook
driver.get("https://www.facebook.com/")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xkjl1po > .x1lliihq'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x1a2a7pz > .x16tdsg8'))).send_keys(narasi)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x12mruv9:nth-child(2) .x1b0d499:nth-child(1)'))).click()
photo_element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
photo_element.send_keys(allimage)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xtk6v10 > .x1lliihq'))).click()
time.sleep(5)

## Twitter
driver.get("https://twitter.com/")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-901oao > div > .css-1dbjc4n > .css-901oao > .css-901oao'))).click()
WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root'))).click()
text1 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
ActionChains(driver).move_to_element(text1).send_keys(allimage).perform()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//input[@accept]'))).send_keys(narasi)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'))).click()
time.sleep(60)

## Telegram
apiToken = '5663329448:AAFYtirH9HbrgcsJWPisd-blu-AL1jV0Aes'
chatID = '-38488324'
bot = Bot(token=apiToken)
bot.send_media_group(chat_id=chatID,media=[imp(open(folderNDF+"kabupaten.png", 'rb'), caption=narasi)
                    #, imp(open(folderMar+bsk+".png", 'rb'))
                    ])