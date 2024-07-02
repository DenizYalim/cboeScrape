import selenium
from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options

print("Start cboe tablo çekme")

options = Options()  #webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get('https://www.cboe.com/tradable_products/vix/vix_futures/')

source = driver.page_source

allRowsHtml = []

def getLines(very_long_string, starter, ender):
    testString = starter + '(.*?)' + ender
    matches = re.findall(testString, very_long_string)
    for match in matches:       #TODO: We probably don't need to create matches and go though it again, just write it inside it
        arr2 = []
        arr2.append(''.join(match))
        #print(match)
    return arr2

allRowsHtml = getLines(source, 'tr role="row"', "</tr>")

allRows = []
def getKeys(starter_data, ender_data):
    for i in allRowsHtml:
        allRows = getLines(i, starter_data, ender_data)
        print(allRows)

    pass

getKeys('fOvMUL">', "</div>")


print("\n")
driver.quit()