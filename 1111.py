import pickle
import undetected_chromedriver as uc
from selenium import webdriver
import time

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    browser = uc.Chrome(
        options=options,
    )
    browser.get('https://twitter.com/')
    time.sleep(240)


    cookies = browser.get_cookies()

    pickle.dump(cookies, open("twitter.pkl", "wb"))