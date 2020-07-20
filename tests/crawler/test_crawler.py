from tibia.crawler import Crawler
from downloader import Downloader


def test_tibia_search_character():
        crawler = Crawler("https://www.tibia.com/","Bobo",Downloader())