import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')

def Massacre():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/August_22nd_Event-Discussion_Massacre')
    ClickToEndSpecordWiki.SkinEvents()


def Migration():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Discord_Migration_of_2016')
    ClickToEndSpecordWiki.SkinEvents()

def MCMessenger():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/MCMessenger_ARG')
    ClickToEndSpecordWiki.SkinEvents()

def Screenshot():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Screen_Shot_2019-06-18_at_2.31.18_AM')
    ClickToEndSpecordWiki.SkinEvents()

def Gala(): 
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Special_Gala_Event')
    ClickToEndSpecordWiki.SkinEvents()
	

def Spongebob(): 
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Spongebob_helps_Genji_with_his_math_homework')
    ClickToEndSpecordWiki.SkinEvents()

def Bot_Chat(): 
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Bot-Chat_Purge')
    ClickToEndSpecordWiki.SkinEvents()

def Meeting_of_the_minds(): 
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Meeting_of_Minds')
    ClickToEndSpecordWiki.SkinEvents()