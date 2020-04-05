import os
import re


import requests
from bs4 import BeautifulSoup as bs

FILTER_URL = "https://dova-s.jp/_contents/settingSound/run.html?time=5"
BASE_URL = "https://dova-s.jp/bgm/index.html?page="
POST_BASE_URL = "https://dova-s.jp"
YOUTUBE_LINK_PATTERN = r"https://www.youtube.com/embed/.*?(?=\")"

class DovaScraper:
    def __init__(self, value):
        self.value = value
    def setName(self):
        pass

def main():
    with requests.Session() as s:
        filter_response = s.get(FILTER_URL)
        page = 1
        while True:
            response = s.get(BASE_URL+str(page))
            if "404 FILE NOT FOUND" in response.text:
                break
            soup = bs(response.text, "html.parser")

            for song_element in soup.select("#itemList > dl"):
                second = int(song_element.select("li")[2].text.replace("duration2:","").replace("~",""))

                if 14 <= second <= 17:
                    post_link = POST_BASE_URL + song_element.select("dt > p > a")[0]["href"]
                    response = s.get(post_link)
                    soup = bs(response.text, "html.parser")
                    youtube_link = re.compile(YOUTUBE_LINK_PATTERN).search(response.text).group()
                    
                    with open("dova_youtube_links.txt",encoding="utf-8",mode="a") as f:
                        f.write(youtube_link + "\n")
                    print(youtube_link)
            print(str(page) + "Page Done.")
            page = page + 1


if __name__ == "__main__":
    main()