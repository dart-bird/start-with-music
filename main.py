import logging
import random
import time
import os
import pyperclip
from bs4 import BeautifulSoup
from playsound import playsound
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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

# Init webdriver
music_driver = webdriver.Chrome(webdriver_path, chrome_options= chrome_options)

# Init start link
initLink = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhazRyWjBFRjlCenhOSVFBUG9ubGRYeA%3D%3D"

# Func
def StartWithChrome():
    
    music_driver.get(initLink)
    youtubeList = music_driver.find_elements_by_id('video-title')
    youtubeList[random.randint(0,len(youtubeList)-1)].click()

StartWithChrome()