import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = uc.Chrome(
        options=options,
    )
    browser.get('https://twitter.com')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        cookie['domain'] = ".twitter.com"
        
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    browser.get('https://twitter.com/home')

    time.sleep(5)

    cookies = browser.get_cookies()

    pickle.dump(cookies, open("cookies.pkl", "wb"))

    time.sleep(120)