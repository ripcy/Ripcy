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
try:
    os.makedirs("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF")
except FileExistsError:
    # directory already exists
    pass
folderIBF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF/")
src = "https://web.meteo.bmkg.go.id//media/data/bmkg/ibfnew/34_papua_24.png"
urllib.request.urlretrieve(src, folderIBF+bsk+".png")
image = os.path.realpath(folderIBF+bsk+".png")
narasi = ("Informasi Prakiraan Cuaca Berbasis Dampak wilayah Provinsi Papua berlaku "+tanggalbesok+" pukul 09.00 WIT - "+tanggallusa+" pukul 09.00 WIT Informasi lebih lengkap dapat diakses pada : http://signature.bmkg.go.id/")

## Setting Chrome Driver
currentPath = __file__.split("Whatsapp.py")[0] 
driverPath = 'C:/Coding/Script/Ripcy/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(driverPath, options=chromeOptions)

#if len(nomor) == 0:
#    driver.get("http://web.whatsapp.com")
#else:
#    driver.get("https://web.whatsapp.com/send?phone="+nomor+"&text&type=phone_number&app_absent=1")

'''Whatsapp
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("My Wifi", Keys.ENTER)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(image)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'))).send_keys(narasi)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
'''


### Facebook
driver.get("https://www.facebook.com/arif.ripcy")
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.lc19xlkw > .b6ax4al1'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r55ey5z8:nth-child(2) .i85zmo3j'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_/8"]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]'))).send_keys(narasi)
#driver.execute_script("window.open('');")
#driver.switch_to.window(driver.window_handles[1])


'''#driver.get("https://web.telegram.org/")
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="folders-container"]/div/div[1]/ul/a[1]/div[1]'))).click()
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]'))).click()
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]'))).send_keys(Keys.CONTROL, 'v')
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[3]/div[1]'))).send_keys(narasi)
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[1]/button'))).click()
'''
'''
import requests

url = "https://api.telegram.org/bot5663329448:AAFYtirH9HbrgcsJWPisd-blu-AL1jV0Aes/sendPhoto"

payload = {
    "photo": image,
    "caption": narasi,
    "disable_notification": False,
    "reply_to_message_id": None
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)

'''
'''
#time.sleep(5)
#driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').send_keys("Info BMKG Papua", Keys.ENTER)
#time.sleep(1)
#driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(Keys.CONTROL, 'v')
#time.sleep(2)
#driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]').send_keys(narasi)
#driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div').click()
#time.sleep(10)
'''

driver.quit()
