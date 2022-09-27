from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from io import BytesIO
import win32clipboard
from PIL import Image
def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

#filepath = 'Ico2.png'
image = Image.open("D:/TAHUN 2022/9. SEPTEMBER/NDF/11092022/kabupaten.png")

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)


currentPath = __file__.split("Whatsapp.py")[0] 
driverPath = 'C:/Ripcy/Script_1/Ripcy-1/chromedriver.exe' 

chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=" + currentPath + "cookies")

driver = webdriver.Chrome(driverPath, options=chromeOptions)

driver.get("http://web.whatsapp.com")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
ActionChains(driver)\
    .send_keys("Arif", Keys.ENTER)\
    .perform()

driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]').send_keys(Keys.CONTROL, 'v')

#time.sleep(30)


#driver.get("https://web.telegram.org")
#time.sleep(15)
