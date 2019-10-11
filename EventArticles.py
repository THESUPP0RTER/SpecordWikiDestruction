import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')


def EventDiscussionMassacre():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/August_22nd_Event-Discussion_Massacre')
    ClickToEndSpecordWiki.SkinEvent()


def DiscordMigration():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Discord_Migration_of_2016')
    ClickToEndSpecordWiki.SkinEvent()


def MCM():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/MCMessenger_ARG')
    ClickToEndSpecordWiki.SkinEvent()


def Gala():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Special_Gala_Event')
    ClickToEndSpecordWiki.SkinEvent()


def SpongebobHelps():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Spongebob_helps_Genji_with_his_math_homework')
    ClickToEndSpecordWiki.SkinEvent()


def BotChatPurge():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Bot-Chat_Purge')
    ClickToEndSpecordWiki.SkinEvent()


def MeetingOfMinds():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Meeting_of_Minds')
    ClickToEndSpecordWiki.SkinEvent()
