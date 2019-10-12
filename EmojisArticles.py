import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')

def Bunblush():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Bunblush:')
    ClickToEndSpecordWiki.SkinEmoji()


def List():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/List_of_Emojis_in_Specord')
    ClickToEndSpecordWiki.SkinEmoji()


def Yeah():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Yeah_(:yeah:)')
    ClickToEndSpecordWiki.SkinEmoji()


def YellowD():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/YellowD:')
    ClickToEndSpecordWiki.SkinEmoji()

