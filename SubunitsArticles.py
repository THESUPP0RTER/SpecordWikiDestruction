import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')


def DottoSquad():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Dotto_Squad')
    ClickToEndSpecordWiki.SkinSubunits()

def Twenty17Gang():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/2017_Gang')
    ClickToEndSpecordWiki.SkinSubunits()
def FebruaryGang():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/February_Gang')
    ClickToEndSpecordWiki.SkinSubunits()

