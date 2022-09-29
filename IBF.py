###  Import Module
import time
import urllib.request
from PIL import Image
import win32clipboard
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tanggal import thnskr, bulanangka, bulan, bsk, tanggalbesok, tanggallusa

### Setting Clipbord
def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

### File yang di upload dan narasi
folderIBF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF/")
src = "https://web.meteo.bmkg.go.id//media/data/bmkg/ibfnew/34_papua_24.png"
urllib.request.urlretrieve(src, folderIBF+bsk+".png")
image = Image.open(folderIBF+bsk+".png")
narasi = ("Informasi Prakiraan Cuaca Berbasis Dampak wilayah Provinsi Papua berlaku "+tanggalbesok+" pukul 09.00 WIT - "+tanggallusa+" pukul 09.00 WIT Informasi lebih lengkap dapat diakses pada : http://signature.bmkg.go.id/")

### Passing File to Clipbord
output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()
send_to_clipboard(win32clipboard.CF_DIB, data)

## Setting Chrome Driver
currentPath = __file__.split("Whatsapp.py")[0] 
driverPath = 'C:/Ripcy/Script_1/Ripcy-1/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(driverPath, options=chromeOptions)

driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Arif", Keys.ENTER)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))).send_keys(Keys.CONTROL, 'v')
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'))).send_keys(narasi)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get("https://web.telegram.org/")
time.sleep(20)

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

driver.close()
