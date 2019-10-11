import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')


def SpecordStaff():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Specord_Staff')
    ClickToEndSpecordWiki.SkinSpecordStaff()