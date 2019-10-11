import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')


def Clowns():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Clowns')
    ClickToEndSpecordWiki.SkinGroup()


def LordsOfSpecord():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Lords_of_Specord')
    ClickToEndSpecordWiki.SkinGroup()

