# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://seleniumhq.org/')

import time
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/acer/Downloads/chromedriver_win32/chromedriver.exe')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()