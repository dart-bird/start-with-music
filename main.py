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


class Music_player:
    music_driver = None

    def __init__(self, input_driver):
        super().__init__()
        self.music_driver = input_driver

    def _youtube_select_random_search_query(self, search_query):
        currentPlayTitle = search_query[random.randint(0, len(searchTitle) - 1)]
        print("Today Song Picked PlayList ~ %s" % currentPlayTitle)
        return "https://www.youtube.com/results?search_query=" + currentPlayTitle

    def youtube_playList(self, playlist_link):
        # EX) playlist_link = "https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlhazRyWjBFRjlCenhOSVFBUG9ubGRYeA%3D%3D"
        self.music_driver.get(playlist_link)
        youtubeList = self.music_driver.find_elements_by_id("video-title")
        youtubeList[random.randint(0, len(youtubeList) - 1)].click()

    def youtube_play(self, search_query):
        self.music_driver.get(self._youtube_select_random_search_query(search_query))
        youtubeList = self.music_driver.find_elements_by_id("video-title")
        youtubeList[random.randint(0, len(youtubeList) - 1)].click()


if __name__ == "__main__":
    music_player = Music_player(input_driver=music_driver)
    music_player.youtube_play(search_query=searchTitle)
