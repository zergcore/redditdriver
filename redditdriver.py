from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH=r"C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)

driver.get("https://www.reddit.com")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("sellingnudes")
search.send_keys(Keys.RETURN) #Enter

time.sleep(60)

driver.quit()