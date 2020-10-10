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

# Init start link title
myfile = open("./targetSearch.txt", "r+", encoding="utf8")
searchTitle = myfile.readlines()
myfile.close()
print("Total Search Title ~ ", searchTitle)
# Init webdriver
music_driver = webdriver.Chrome(webdriver_path, options=chrome_options)


# Func
class StartWithChrome():
    def youtube_playList(self):
        music_driver.get(
            'https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhazRyWjBFRjlCenhOSVFBUG9ubGRYeA%3D%3D'
        )
        youtubeList = music_driver.find_elements_by_id('video-title')
        youtubeList[random.randint(0, len(youtubeList) - 1)].click()

    def youtube_searchList(self):
        currentPlayTitle = searchTitle[random.randint(0, len(searchTitle) - 1)]
        print("Today Song Picked PlayList ~ %s" % currentPlayTitle)
        initLink = "https://www.youtube.com/results?search_query=" + currentPlayTitle
        music_driver.get(initLink)
        youtubeList = music_driver.find_elements_by_id('video-title')
        youtubeList[random.randint(0, len(youtubeList) - 1)].click()


StartWithChrome.youtube_searchList(self=None)