from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from time import sleep

#Close popups
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

#Abrir el driver, y con el driver abrir el navegador
driver = webdriver.Chrome(chrome_options=option, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
driver.get("https://www.reddit.com/")
print(driver.title) 

login=driver.find_element_by_link_text("Log In")
login.click()

username = ""          # Enter your username
password = ""              # Enter your password

def slow_typing(element, text):
    for character in text: 
      element.send_keys(character)
      sleep(0.3)

def logIn():            # Log In Function.
    try:
        driver.switch_to.frame(driver.find_element_by_tag_name('iframe')) 
        sleep(15)
        
        username_in = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='loginUsername']")))
        slow_typing(username_in, username)

        pass_in = driver.find_element_by_xpath("//*[@id='loginPassword']")
        slow_typing(pass_in,password)

        driver.find_element(By.XPATH, "//button[@class='AnimatedForm__submitButton m-full-width']").click()

        sleep(5)
        driver.switch_to.default_content()
    except NoSuchElementException:
        driver.switch_to.default_content()
        print("Llegue aqui xd xd")

logIn()
