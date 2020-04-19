import logging
import random
import time

import pyperclip
from bs4 import BeautifulSoup
from playsound import playsound
from selenium import webdriver
from selenium.common.exceptions import (NoSuchElementException,
                                        WebDriverException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

initLink = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhazRyWjBFRjlCenhOSVFBUG9ubGRYeA%3D%3D"
music_driver = webdriver.Chrome("./chromedriver.exe")

def StartWithChrome():
    music_driver.get(initLink)
    youtubeList = music_driver.find_element_by_id('video-title')
    print(youtubeList)

StartWithChrome()