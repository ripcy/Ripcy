#####################################  Import Module  #####################################
import os, os.path, time, urllib.request, calendar, locale, pathlib
from PIL import Image
from datetime import date, datetime,timedelta
from telegram import Bot, InputMediaPhoto as imp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
chromeService = Service(driverPath)
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")
#chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(service=chromeService, options=chromeOptions)
###########################################################################################


##################################  Upload to Whatsapp  ###################################
driver.get("http://web.whatsapp.com")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'))).send_keys("Arif Ripcy", Keys.ENTER)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="clip"]/..'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer//*[@data-icon="attach-image"]/../input'))).send_keys(file)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]'))).send_keys(text)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div'))).click()
###########################################################################################

##################################  Upload to Telegram  ###################################
apiToken = '5663329448:AAFYtirH9HbrgcsJWPisd-blu-AL1jV0Aes'
chatID = '40071216'
bot = Bot(token=apiToken)
bot.send_media_group(chat_id=chatID,media=[imp(open(file, 'rb'), caption=text)])
###########################################################################################

##################################  Upload to Facebook  ###################################
driver.get("https://www.facebook.com/")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xkjl1po > .x1lliihq'))).click()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x1a2a7pz > .x16tdsg8'))).send_keys(text)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.x12mruv9:nth-child(2) .x1b0d499:nth-child(1)'))).click()
photo_element = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
photo_element.send_keys(file)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xtk6v10 > .x1lliihq'))).click()
###########################################################################################

###################################  Upload to Instagram  #################################
driver.get('https://www.instagram.com/')
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_acub .\_ab6-'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//input[@accept='image/jpeg,image/png,image/heic,image/heif,video/mp4,video/quicktime']"))).send_keys(file)
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_ab8w:nth-child(1) > .\_ab8w .\_abfz .\_ab6-'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_acan:nth-child(1) > .\_ab8w > .\_ab8w > .\_aacl'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_ab99 > .\_acan'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_ab99 > .\_acan'))).click()
WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.\_aaeg'))).send_keys(text)
WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Share']"))).click()
###########################################################################################

###################################  Upload to Twitter  ###################################
driver.get("https://twitter.com/")
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-901oao > div > .css-1dbjc4n > .css-901oao > .css-901oao'))).click()
WebDriverWait(driver, 200).until(EC.element_to_be_clickable((By.CLASS_NAME, 'DraftEditor-root'))).click()
text1 = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, 'public-DraftEditorPlaceholder-root')))
ActionChains(driver).move_to_element(text1).send_keys(text).perform()
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//input[@accept]'))).send_keys(file)
WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'))).click()
