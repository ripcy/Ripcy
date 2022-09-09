from optparse import Option
from turtle import right
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import urllib
import ssl
from PIL import Image
from tanggal import besok
import os

# Setting
service = FirefoxService(executable_path=GeckoDriverManager().install())
options = FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

os.mkdir = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/IBF")

folderNDF = ("D:/TAHUN "+thnskr+"/"+str (bulanangka)+". "+bulan+"/NDF/"+bsk+"/")

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# 1 | open | https://172.19.22.55/ | 
driver.get("https://172.19.22.55/")
# 2 | setWindowSize | 1140x900 | 
driver.set_window_size(1920, 1080)
driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "password").send_keys("fodpapua5jay")
driver.find_element(By.ID, "username").send_keys("FODPAPUA")
driver.find_element(By.ID, "signin").click()
driver.find_element(By.ID, "badge_producer").click()

# 3 | click | css=#row_7694 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7694 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"asmat.png")
# 4 | click | css=.ui-button-text | 
driver.find_element(By.CSS_SELECTOR, ".ui-button-text").click()

# 5 | click | css=#row_7695 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7695 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"biak.png")
# 6 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 7 | click | css=#row_7696 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7696 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"boven.png")
# 8 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()


# 9 | click | css=#row_7697 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7697 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"deiyai.png")
# 10 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 11 | click | css=#row_7698 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7698 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"dogiyai.png")
# 12 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 13 | click | css=#row_7699 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7699 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"intan.png")
# 14 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 27 | click | css=#row_7700 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7700 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"jayawijaya.png")
# 28 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 29 | click | css=#row_7701 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7701 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"keerom.png")
# 30 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 31 | click | css=#row_7702 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7702 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"yapen.png")
# 32 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 33 | click | css=#row_7703 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7703 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"lanny.png")
# 34 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 35 | click | css=#row_7704 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7704 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"mamberaya.png")
# 36 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 37 | click | css=#row_7705 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7705 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"mamteng.png")
# 38 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 39 | click | css=#row_7706 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7706 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"mappi.png")
# 40 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 41 | click | css=#row_7707 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7707 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"merauke.png")
# 42 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 43 | click | css=#row_7708 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7708 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"mimika.png")
# 44 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 45 | click | css=#row_7709 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7709 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"nabire.png")
# 46 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 47 | click | css=#row_7710 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7710 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"ndunga.png")
# 48 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 49 | click | css=#row_7711 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7711 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"paniai.png")
# 50 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 51 | click | css=#row_7712 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7712 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"bintang1.png")
# 52 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 53 | click | css=#row_7713 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7713 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"puncak.png")
# 54 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 55 | click | css=#row_7714 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7714 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"sarmi.png")
# 56 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 57 | click | css=#row_7715 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7715 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"supiori.png")
# 58 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 59 | click | css=#row_7716 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7716 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"toli1.png")
# 60 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 61 | click | css=#row_7717 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7717 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"waropen.png")
# 62 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 63 | click | css=#row_7718 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7718 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"yahu1.png")
# 64 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 65 | click | css=#row_7719 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7719 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"yalimo.png")
# 66 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 67 | click | css=#row_7720 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_7720 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"jprkota.png")
# 68 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 69 | click | css=#row_8011 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_8011 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"jprkab.png")
# 70 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 71 | click | css=#row_8012 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_8012 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"bintang2.png")
# 72 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 73 | click | css=#row_8013 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_8013 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"toli2.png")
# 74 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 75 | click | css=#row_8014 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_8014 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"yahu2.png")
# 76 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 77 | click | css=#row_8015 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_8015 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"yahu3.png")
# 78 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 79 | click | css=#row_13063 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_13063 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"1.png")
# 80 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()

# 81 | click | css=#row_13064 .aLien1:nth-child(1) > img | 
driver.find_element(By.CSS_SELECTOR, "#row_13064 .aLien1:nth-child(1) > img").click()
img = driver.find_element(By.CLASS_NAME, "zoomedOut")
src = img.get_attribute('src')
urllib.request.urlretrieve(src, folderNDF+"2.png")
# 82 | click | css=.ui-icon-closethick | 
driver.find_element(By.CSS_SELECTOR, ".ui-icon-closethick").click()




from PIL import Image
from tanggal import besok,sekarang
######### Crop
asmat = Image.open(folderNDF+"asmat.png").crop((0, 0, 744, 609)).save(folderNDF+"asmat.png")
biak = Image.open(folderNDF+"biak.png").crop((0, 0, 744, 960)).save(folderNDF+"biak.png")
bintang1 = Image.open(folderNDF+"bintang1.png").crop((0, 0, 744, 928)).save(folderNDF+"bintang1.png")
bintang2 = Image.open(folderNDF+"bintang2.png").crop((0, 0, 744, 898)).save(folderNDF+"bintang2.png")
boven = Image.open(folderNDF+"boven.png").crop((0, 0, 744, 1052)).save(folderNDF+"boven.png")
deiyai = Image.open(folderNDF+"deiyai.png").crop((0, 0, 744, 574)).save(folderNDF+"deiyai.png")
dogiyai = Image.open(folderNDF+"dogiyai.png").crop((0, 0, 744, 670)).save(folderNDF+"dogiyai.png")
intan = Image.open(folderNDF+"intan.png").crop((0, 0, 744, 610)).save(folderNDF+"intan.png")
jayawijaya = Image.open(folderNDF+"jayawijaya.png").crop((0, 0, 744, 832)).save(folderNDF+"jayawijaya.png")
jprkab = Image.open(folderNDF+"jprkab.png").crop((0, 0, 744, 929)).save(folderNDF+"jprkab.png")
jprkota = Image.open(folderNDF+"jprkota.png").crop((0, 0, 744, 581)).save(folderNDF+"jprkota.png")
keerom = Image.open(folderNDF+"keerom.png").crop((0, 0, 744, 612)).save(folderNDF+"keerom.png")
lanny = Image.open(folderNDF+"lanny.png").crop((0, 0, 744, 673)).save(folderNDF+"lanny.png")
mamberaya = Image.open(folderNDF+"mamberaya.png").crop((0, 0, 744, 548)).save(folderNDF+"mamberaya.png")
mamteng = Image.open(folderNDF+"mamteng.png").crop((0, 0, 744, 644)).save(folderNDF+"mamteng.png")
mappi = Image.open(folderNDF+"mappi.png").crop((0, 0, 744, 741)).save(folderNDF+"mappi.png")
merauke = Image.open(folderNDF+"merauke.png").crop((0, 0, 744, 1052)).save(folderNDF+"merauke.png")
mimika = Image.open(folderNDF+"mimika.png").crop((0, 0, 744, 803)).save(folderNDF+"mimika.png")
nabire = Image.open(folderNDF+"nabire.png").crop((0, 0, 744, 867)).save(folderNDF+"nabire.png")
ndunga = Image.open(folderNDF+"ndunga.png").crop((0, 0, 744, 646)).save(folderNDF+"ndunga.png")
paniai = Image.open(folderNDF+"paniai.png").crop((0, 0, 744, 613)).save(folderNDF+"paniai.png")
puncak = Image.open(folderNDF+"puncak.png").crop((0, 0, 744, 772)).save(folderNDF+"puncak.png")
sarmi = Image.open(folderNDF+"sarmi.png").crop((0, 0, 744, 677)).save(folderNDF+"sarmi.png")
supiori = Image.open(folderNDF+"supiori.png").crop((0, 0, 744, 549)).save(folderNDF+"supiori.png")
toli1 = Image.open(folderNDF+"toli1.png").crop((0, 0, 744, 961)).save(folderNDF+"toli1.png")
toli2 = Image.open(folderNDF+"toli2.png").crop((0, 0, 744, 962)).save(folderNDF+"toli2.png")
waropen = Image.open(folderNDF+"waropen.png").crop((0, 0, 744, 518)).save(folderNDF+"waropen.png")
yahu1 = Image.open(folderNDF+"yahu1.png").crop((0, 0, 744, 962)).save(folderNDF+"yahu1.png")
yahu2 = Image.open(folderNDF+"yahu2.png").crop((0, 0, 744, 962)).save(folderNDF+"yahu2.png")
yahu3 = Image.open(folderNDF+"yahu3.png").crop((0, 0, 744, 931)).save(folderNDF+"yahu3.png")
yalimo = Image.open(folderNDF+"yalimo.png").crop((0, 0, 744, 581)).save(folderNDF+"yalimo.png")
yapen = Image.open(folderNDF+"yapen.png").crop((0, 0, 744, 805)).save(folderNDF+"yapen.png")
im1 = Image.open(folderNDF+"1.png").crop((0, 0, 744, 1028))
im2 = Image.open(folderNDF+"2.png").crop((0, 88, 744, 820))


newimage = Image.new("RGB", (744, 1775), "white")
newimage.paste(im1, (0,0))
newimage.paste(im2, (0,1028))
newimage.save(folderNDF+"kabupaten.png")

driver.close()
