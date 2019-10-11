import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')


def ArtDiscussion():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Art-discussion')
    ClickToEndSpecordWiki.SkinChannel()

def BotChat():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Bot-chat')
    ClickToEndSpecordWiki.SkinChannel()

def FE():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Fe3h-discussion')
    ClickToEndSpecordWiki.SkinChannel()

def FreeChat():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Free-chat')
    ClickToEndSpecordWiki.SkinChannel()

def Gameverse():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Gameverse')
    ClickToEndSpecordWiki.SkinChannel()
def General():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/General')
    ClickToEndSpecordWiki.SkinChannel()

def HallOfShame():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Hall_of_Shame')
    ClickToEndSpecordWiki.SkinChannel()

def MangaChat():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Manga-chat')
    ClickToEndSpecordWiki.SkinChannel()

def NSFW():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/NSFW-YAOI')
    ClickToEndSpecordWiki.SkinChannel()

def Shipping():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Shipping_Chat')
    ClickToEndSpecordWiki.SkinChannel()

def VC():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/VC')
    ClickToEndSpecordWiki.SkinChannel()