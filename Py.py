import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

pyautogui.hotkey("ctrl", "Alt", "c")
time.sleep(5)
pyautogui.write("https://twitter.com/")
pyautogui.hotkey("enter")
driver = webdriver.Chrome("C:/Coding/R/Ripcy/chromedriver.exe")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span/div/div/span/span').click()

