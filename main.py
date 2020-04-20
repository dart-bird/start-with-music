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

webdriver_path = "./chromedriver.exe"
initLink = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhazRyWjBFRjlCenhOSVFBUG9ubGRYeA%3D%3D"

music_driver = webdriver.Chrome(webdriver_path)

#Extensions
youtubeAdBlock = ".\\chromeExtensions\\youtubeAdBlock\\youtubeAdBlock_extension.crx"
youtubeNoneStop = ".\\chromeExtensions\\youtubeNoneStop\\youtubeNoneStop_extension.crx"

def SettingExtension(webdriver_path):
    os.environ["webdriver.chrome.driver"] = webdriver_path
    chrome_options = Options()
    chrome_options.add_extension(youtubeAdBlock)
    chrome_options.add_extension(youtubeNoneStop)

def StartWithChrome():
    music_driver.get(initLink)
    youtubeList = music_driver.find_elements_by_id('video-title')
    youtubeList[random.randint(0,len(youtubeList)-1)].click()

SettingExtension(webdriver_path=webdriver_path)
StartWithChrome()