import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')


def BenSermon():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ben_Lee%27s_Final_Sermon')
    ClickToEndSpecordWiki.BenSermonPage()
