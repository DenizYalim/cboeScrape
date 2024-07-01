import selenium
from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options

print("Start cboe tablo çekme")

options = Options()  #webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.get('https://www.cboe.com/tradable_products/vix/vix_futures/')

source = driver.page_source


def getKeys(very_long_string, starter, ender):
    testString = starter + '(.*?)' + ender
    matches = re.findall(testString, very_long_string)
    print(matches)


getKeys(source, 'fOvMUL">', "</div>")

print("\n")
driver.quit()
