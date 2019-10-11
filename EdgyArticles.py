import ClickToEndSpecordWiki
from selenium import webdriver
import time

driver = webdriver.Chrome('\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe')


def PokemonSpecial():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Pokemon_Special')
    ClickToEndSpecordWiki.SkinEdgy()

def SpongebobWelcome():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Spongebob_Welcome_to_the_Black_Parade')
    ClickToEndSpecordWiki.SkinEdgy()