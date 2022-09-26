import pickle
import undetected_chromedriver as uc
from selenium import webdriver
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = uc.Chrome(
        options=options,
    )
    browser.get('https://web.whatsapp.com/')
    time.sleep(90)
    browser.get('https://web.telegram.org/')
    time.sleep(90)
    browser.get('https://www.facebook.com/')
    time.sleep(90)
    browser.get('https://twitter.com/')
    time.sleep(90)
    browser.get('https://www.instagram.com/')
    time.sleep(90)

    cookies = browser.get_cookies()

    pickle.dump(cookies, open("cookies.pkl", "wb"))