from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

mov = input("Movie: ")
loc = input("Location: ")
dat = input("Date: ")
tim = input("Time of day: ")

def function():
    driver.get("https://www.google.com")
    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys(mov + " " + loc + " " + dat + " " + tim)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(3)
    driver.save_screenshot('ss.png')
    screenshot = Image.open('ss.png')
    screenshot.show()

def launchBrowser():
    function()
    while(True):
       pass
launchBrowser()
