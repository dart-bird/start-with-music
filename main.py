import logging
import random
import time
import os

# import pyperclip
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# WebDriver Path
webdriver_path = "./chromedriver.exe"

# Extensions Path
youtubeAdBlock = "./chromeExtensions/youtubeAdBlock/youtubeAdBlock_extension.crx"
youtubeNoneStop = "./chromeExtensions/youtubeNoneStop/youtubeNoneStop_extension.crx"

# WebDriver Settings
os.environ["webdriver.chrome.driver"] = webdriver_path
chrome_options = Options()
chrome_options.add_extension(youtubeAdBlock)
chrome_options.add_extension(youtubeNoneStop)

# Init start link
myfile = open("./targetLink.txt", "r+", encoding="utf8")
initLink = myfile.readline()
myfile.close()
print(initLink)

# Init webdriver
music_driver = webdriver.Chrome(webdriver_path, options=chrome_options)


# Func
def StartWithChrome():

    music_driver.get(initLink)
    youtubeList = music_driver.find_elements_by_id('video-title')
    youtubeList[random.randint(0, len(youtubeList) - 1)].click()


StartWithChrome()