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

### File yang di upload dan narasi
folderIBF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/MEDSOS/")
image = os.path.realpath(folderIBF+skr+".mp4")
narasi = ("Hallo #SobatBMKG Berikut admin bagikan update informasi prakiraan cuaca hari ini untuk Kota Jayapura, Kab. Keerom dan sekitarnya "+hariini+", "+tanggalsekarang)

## Setting Chrome Driver
import pathlib
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(driverPath, options=chromeOptions)

##Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Arif Ripcy", Keys.ENTER)
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(image)
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]'))).send_keys(narasi)
WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

##Twitter
driver.get("https://twitter.com/")
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-901oao > div > .css-1dbjc4n > .css-901oao > .css-901oao'))).click()
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root'))).click()
text1 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
ActionChains(driver).move_to_element(text1).send_keys(narasi).perform()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//input[@accept]'))).send_keys(image)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'))).click()

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])

driver.get("https://www.facebook.com/")
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.lc19xlkw > .b6ax4al1'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r55ey5z8:nth-child(1) .i85zmo3j'))).click()
time.sleep(10)
post_box=driver.find_element(By.XPATH, '//*[@id="mount_0_0_2T"]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]')
post_box.send_keys(narasi)
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))).send_keys(image)
photo_element = driver.find_element(By.XPATH,'//input[@type="file"]')
photo_element.send_keys(image)