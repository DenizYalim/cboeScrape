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
    return matches

allRowsHtml = getLines(source, 'tr role="row"', "</tr>")

table_2d = []
for row in allRowsHtml:
    table_2d.append(getLines(row, 'fOvMUL">', "</div>"))

print(table_2d)

print("\n")
driver.quit()