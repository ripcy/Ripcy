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

'''
def __init__(self, browser=None, time_out=600):
    self.browser = browser
    wait = WebDriverWait(browser, time_out)
def find_attachment(self):
    clipButton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..')))
    clipButton.click()
def send_picture(self, picture):
    try:
        filename = os.path.realpath(picture)
        self.find_attachment()
        imgButton = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input',))).send_keys(filename)
        self.send_attachment()
    
    finally:
        print("send_picture() finished running!")
'''

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
'''
#if len(nomor) == 0:
#    driver.get("http://web.whatsapp.com")
#else:
#    driver.get("https://web.whatsapp.com/send?phone="+nomor+"&text&type=phone_number&app_absent=1")
'''
driver.get("https://web.whatsapp.com/send?phone=+6282248864334&text&type=phone_number&app_absent=1")

WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Arif", Keys.ENTER)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(image)
time.sleep(300)

#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(Keys.CONTROL, 'v')
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'))).send_keys(narasi)
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
#driver.execute_script("window.open('');")
#driver.switch_to.window(driver.window_handles[1])
#driver.get("https://web.telegram.org/")
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="folders-container"]/div/div[1]/ul/a[1]/div[1]'))).click()
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]'))).click()
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="column-center"]/div/div/div[4]/div/div[1]/div/div[8]/div[1]/div[1]'))).send_keys(Keys.CONTROL, 'v')
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[3]/div[1]'))).send_keys(narasi)
#WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div[1]/button'))).click()



    