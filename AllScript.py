#####################################  Import Module  #####################################
import os, os.path, time, urllib.request, calendar, locale, pathlib
from PIL import Image
from datetime import date, datetime,timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
###########################################################################################

#####################################  Setting waktu  #####################################
locale.setlocale(locale.LC_TIME, 'id_ID')
today = date.today()
yesterday = today - timedelta(days=1)
yesterday2 = today - timedelta(days=2)
tomorrow = today + timedelta(days=1)
tomorrow2 = today + timedelta(days=2)
datetoday = today.day
bulan = calendar.month_name[today.month]
bulan = bulan.upper()
bulanangka = datetime.now().month
hariini = today.strftime("%A")

# date
tglkmrn = yesterday.strftime("%d")
tglskr = today.strftime("%d")
tglbsk = tomorrow.strftime("%d")
blnskr = today.strftime("%m")
thnskr = today.strftime("%Y")

# dd/mm/YY
kmrn = yesterday.strftime("%d%m%Y")
bsk = tomorrow.strftime("%d%m%Y")
skr = today.strftime("%d%m%Y")

# .strftime("%d %B, %Y")
tanggalkemarin = yesterday.strftime("%d %B %Y")
tanggalsekarang = today.strftime("%d %B %Y")
tanggalbesok = tomorrow.strftime("%d %B %Y")
tanggallusa = tomorrow2.strftime("%d %B %Y")
###########################################################################################

################################  Selenium Driver Setting  ################################
cPath = pathlib.Path(__file__).parent.resolve()
currentPath = str(cPath)
driverPath = currentPath+'/chromedriver.exe' 
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(driverPath, options=chromeOptions)
###########################################################################################

##################################  Upload to Whatsapp  ###################################
wa1 = driver.get("http://web.whatsapp.com")
wa2 = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')))
wa3 = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
wa4 = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(image)
wa5 = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'))).send_keys(narasi)
wa6 = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
###########################################################################################