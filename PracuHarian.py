###  Import Module
import pathlib, time
from telegram import Bot, InputMediaPhoto as imp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from tanggal import *

### File yang di upload dan narasi
folder = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/MEDSOS/")
video = folder+skr+".mp4"
narasi = ("Hallo #SobatBMKG Berikut admin bagikan update informasi prakiraan cuaca hari ini untuk Kota Jayapura, Kab. Keerom dan sekitarnya "+hariini+", "+tanggalsekarang)

### Setting Driver
import pathlib
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeService = Service(driverPath)
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.headless = True
driver = webdriver.Chrome(service=chromeService, options=chromeOptions)

## Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Info BMKG Papua", Keys.ENTER)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(video)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]'))).send_keys(narasi)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

## Twitter
driver.get("https://twitter.com/")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-901oao > div > .css-1dbjc4n > .css-901oao > .css-901oao'))).click()
WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root'))).click()
text1 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
ActionChains(driver).move_to_element(text1).send_keys(narasi).perform()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//input[@accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime"]'))).send_keys(video)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'))).click()

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])

## facebook
driver.get("https://www.facebook.com/")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xkjl1po > .x1lliihq'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x1a2a7pz > .x16tdsg8'))).send_keys(narasi)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x12mruv9:nth-child(2) .x1b0d499:nth-child(1)'))).click()
photo_element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
photo_element.send_keys(video)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xtk6v10 > .x1lliihq'))).click()

driver.switch_to.window(driver.window_handles[0])

## Telegram
apiToken = '5663329448:AAFYtirH9HbrgcsJWPisd-blu-AL1jV0Aes'
chatID = '-38488324'
bot = Bot(token=apiToken)
bot.send_video(chat_id=chatID,video=open(video, 'rb'), caption=narasi)

time.sleep(60)
driver.quit()
