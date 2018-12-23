import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'intl.accept_languages': "en-US, en"})
options.add_argument("--start-maximized")

browser = webdriver.Chrome(chrome_options=options)
browser.get('https://www.google.co.uk')

search = browser.find_element_by_name('q')
search.send_keys("humanoid robot")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("hologram")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("doctor strange ps4 pro")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("ironman ps4 pro")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("transparent monitor computer")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("smart glasses")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("The most accurate voice recognition python library")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("deep learning trained model for download to use")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("cv2 finger motion detection")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("python similar semantic sentences generators")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("python similar semantic sentences groups database")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results

search = browser.find_element_by_name('q')
search.clear()
search.send_keys("cv2 hand motion detection")
search.send_keys(Keys.RETURN) # hit return after you enter search text
time.sleep(5) # sleep for 5 seconds so you can see the results
