import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')

def Bunblush():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Bunblush:')
    ClickToEndSpecordWiki.SkinEmoji()

def ListOfEmojis():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/List_of_Emojis_in_Specord')
    ClickToEndSpecordWiki.SkinEmoji()

def ScreenShot():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Screen_Shot_2019-06-18_at_2.31.18_AM')
    ClickToEndSpecordWiki.SkinEmoji()

def Yeah():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Yeah_(:yeah:)')
    ClickToEndSpecordWiki.SkinEmoji()

def YellowD():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/YellowD:')
    ClickToEndSpecordWiki.SkinEmoji()

