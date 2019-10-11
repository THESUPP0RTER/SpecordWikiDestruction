from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import CharacterArticles
import BlogArticles
import ChannelArticles
import EdgyArticles
import EmojiArticles
import EventArticles
import GroupArticles
import LoreArticles
import TextFiles
import ShippingArticles
import SpecordStaffArticles
import SubunitsArticles
import WordsArticles

import time

driver = webdriver.Chrome("\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe")
def Categories():
    #Goes into Categories
    driver.get('https://specord.fandom.com/wiki/Special:Categories')

def DeleteAll():
    #control A, then backspaces a select text
    ctrla = ActionChains(driver)
    ctrla.key_down(Keys.CONTROL)
    ctrla.send_keys("a")
    ctrla.key_up(Keys.CONTROL)
    ctrla.send_keys(Keys.BACK_SPACE)
    ctrla.perform()
def SavePage():
    #types into summary Skin, Skin and presses the publish button
    textbox = '//*[@id="wpSummary"]'
    actio = ActionChains(driver)
    summary = driver.find_element_by_xpath(textbox)
    summary.click()
    actio.send_keys('SKIN, SKIN')
    actio.perform()

    savePage = '//*[@id="wpSave"]'
    btn = driver.find_element_by_xpath(savePage)
    btn.click()
def EditButton():
    #Hovers over the edit dropdown and clicks on the classic editor button
    act = ActionChains(driver)
    id = '//*[@id="PageHeader"]/div[2]/div[2]/div/div/div[1]'
    id2 = 'ca-edit'
    firstlevelbtn = driver.find_element_by_xpath(id)
    act.move_to_element(firstlevelbtn).perform()
    time.sleep(2)
    secondlevelbtn = driver.find_element_by_id(id2)
    secondlevelbtn.click()
    time.sleep(2)
    source = 'cke_26'
    sourcetab = driver.find_element_by_id(source)
    sourcetab.click()

def OutputSkinFileCharacter():
    #Reads the skin character text file and pastes it
    act = ActionChains(driver)
    skin = TextFiles.skincharactertext.read()
    act.send_keys(skin)
    act.perform()
def OutputAloisText():
    #Alois's Page
    act = ActionChains(driver)
    skin = TextFiles.aloistext.read()
    act.send_keys(skin)
    act.perform()
def OutputBenSermon():
    # Reads the skin character text file and pastes it
    act = ActionChains(driver)
    skin = TextFiles.bensermon.read()
    act.send_keys(skin)
    act.perform()
def OutputSkinFileChannel():
    #Reads the skin channel text file and pastes it
    act = ActionChains(driver)
    skin = TextFiles.skinchanneltext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileEdgy():
    act = ActionChains(driver)
    skin = TextFiles.skinedgytext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileEmoji():
    act = ActionChains(driver)
    skin = TextFiles.skinemojitext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileEvent():
    act = ActionChains(driver)
    skin = TextFiles.skineventtext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileGroup():
    act = ActionChains(driver)
    skin = TextFiles.skingrouptext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileLore():
    act = ActionChains(driver)
    skin = TextFiles.skinloretext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileShipping():
    act = ActionChains(driver)
    skin = TextFiles.skinshiptext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileSpecordStaff():
    act = ActionChains(driver)
    skin = TextFiles.skinstafftext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileSubunits():
    act = ActionChains(driver)
    skin = TextFiles.skinsubunitstext
    act.send_keys(skin)
    act.perform()
def OutputSkinFileWords():
    act = ActionChains(driver)
    skin = TextFiles.skinwordstext
    act.send_keys(skin)
    act.perform()



def SkinCharacter():
    #Use this function for a character/member
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileCharacter()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def BenSermonPage():
    #Use this function for Ben Lee's sermon's page
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputBenSermon()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def AloisPage():
    #Use this function for Alois's page
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputAloisText()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinChannel():
    #use this for a specific channel's page
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileChannel()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinEdgy():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileEdgy()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinEmoji():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileEmoji()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinEvent():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileEvent()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinGroup():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileGroup()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinLore():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileLore()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinShipping():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileShipping()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinSpecordStaff():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileSpecordStaff()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinSubunits():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileSubunits()
    time.sleep(1)
    driver.stop_client()
    SavePage()
def SkinWords():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileWords()
    time.sleep(1)
    driver.stop_client()
    SavePage()

def Characters():
#one by one, they all fall down
   CharacterArticles.Aeiriter()
   CharacterArticles.AK()
   CharacterArticles.Ally()
   CharacterArticles.Amarillo()
   CharacterArticles.Ambient()
   CharacterArticles.Ash()
   CharacterArticles.BenLee()
   CharacterArticles.Blue()
   CharacterArticles.Black()
   CharacterArticles.Bullying()
   CharacterArticles.Bots()
   CharacterArticles.Caddy()
   CharacterArticles.Cass()
   CharacterArticles.ChaseKip()
   CharacterArticles.Copper()
   CharacterArticles.Crazed()
   CharacterArticles.Crt()
   CharacterArticles.Crystal()
   CharacterArticles.Deimos()
   CharacterArticles.Ditty()
   CharacterArticles.Ebra()
   CharacterArticles.Eeveechu()
   CharacterArticles.Eggman()
   CharacterArticles.Exvnir()
   CharacterArticles.Falco()
   CharacterArticles.Faust()
   CharacterArticles.Ghay()
   CharacterArticles.Ghfrc()
   CharacterArticles.Gibby()
   CharacterArticles.Gold()
   CharacterArticles.GP()
   CharacterArticles.Green()
   CharacterArticles.Gresh()
   CharacterArticles.Hanamits()
   CharacterArticles.Heartman()
   CharacterArticles.Kusaka()
   CharacterArticles.Jautts()
   CharacterArticles.Kris()
   CharacterArticles.Jolthicc()
   CharacterArticles.Khun()
   CharacterArticles.Lack()
   CharacterArticles.Leaf()
   CharacterArticles.MeTwo()
   CharacterArticles.Mel()
   CharacterArticles.Mha()
   CharacterArticles.Moni()
   CharacterArticles.Moon()
   CharacterArticles.Neris()
   CharacterArticles.Nicole()
   CharacterArticles.NightRiley()
   CharacterArticles.Nobadi()
   CharacterArticles.NobadiAllegedly()
   CharacterArticles.Ozzie()
   CharacterArticles.Pearl()
   CharacterArticles.Pebboe()
   CharacterArticles.PebboeTom()
   CharacterArticles.Piplup()
   CharacterArticles.Plantsuke()
   CharacterArticles.Qami()
   CharacterArticles.Quip()
   CharacterArticles.Rebooted()
   CharacterArticles.Red()
   CharacterArticles.Rei()
   CharacterArticles.Rico()
   CharacterArticles.Rile()
   CharacterArticles.Rita()
   CharacterArticles.Ruby()
   CharacterArticles.Selphie()
   CharacterArticles.Shadow()
   CharacterArticles.Shaun()
   CharacterArticles.Silver()
   CharacterArticles.Sof()
   CharacterArticles.Soft()
   CharacterArticles.Soup()
   CharacterArticles.Spora()
   CharacterArticles.Straw()
   CharacterArticles.Sun()
   CharacterArticles.Specordion()
   CharacterArticles.Supporter()
   CharacterArticles.TomNook()
   CharacterArticles.White()
def BlogPosts():
    BlogArticles.BenSermon()
def Channels():
    ChannelArticles.ArtDiscussion()
    ChannelArticles.BotChat()
    ChannelArticles.FE()
    ChannelArticles.FreeChat()
    ChannelArticles.Gameverse()
    ChannelArticles.General()
    ChannelArticles.HallOfShame()
    ChannelArticles.MangaChat()
    ChannelArticles.NSFW()
    ChannelArticles.Shipping()
    ChannelArticles.VC()
def Edgy():
    EdgyArticles.SpongebobWelcome()
    EdgyArticles.PokemonSpecial()
def Emoji():
    EmojiArticles.Bunblush()
    EmojiArticles.ListOfEmojis()
    EmojiArticles.ScreenShot()
    EmojiArticles.Yeah()
    EmojiArticles.YellowD()
def Event():
    EventArticles.BotChatPurge()
    EventArticles.DiscordMigration()
    EventArticles.EventDiscussionMassacre()
    EventArticles.Gala()
    EventArticles.MCM()
    EventArticles.MeetingOfMinds()
    EventArticles.SpongebobHelps()
def Group():
    GroupArticles.Clowns()
    GroupArticles.LordsOfSpecord()
def Lore():
    LoreArticles.Specord()
def Shipping():
    ShippingArticles.Agency()
    ShippingArticles.Chosen()
    ShippingArticles.EmoOrange()
    ShippingArticles.Frantic()
    ShippingArticles.Laverre()
    ShippingArticles.OldRival()
    ShippingArticles.PreciousMetal()
    ShippingArticles.SimilarToSeddie()
    ShippingArticles.Special()
def Staff():
    SpecordStaffArticles.SpecordStaff()
def Subunits():
    SubunitsArticles.DottoSquad()
    SubunitsArticles.FebruaryGang()
    SubunitsArticles.Twenty17Gang()
def Words():
    WordsArticles.Hot()
    WordsArticles.Normal()

def main():
    driver.get("https://specord.fandom.com/wiki/Specord_Wiki")
    Categories()
    #buffer time, login to burner email
    time.sleep(30)
    Characters()
    Categories()
    BlogPosts()
    Categories()
    Channels()
    Categories()
    Edgy()
    Categories()
    Emoji()
    Categories()
    Event()
    Categories()
    Group()
    Categories()
    Lore()
    Categories()
    Shipping()
    Categories()
    Staff()
    Categories()
    Subunits()
    Categories()
    Words()
    CharacterArticles.Alois()
    driver.close()
main()
