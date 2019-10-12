from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

#declare drivers and text files
driver = webdriver.Chrome("\\Users\Gabe\PycharmProjects\SpecordWiki\drivers\chromedriver.exe")

skincharactertext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\charactertext.txt", 'r')
aloistext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\idea.txt", 'r')
softtext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\soft.txt", 'r')
bensermon = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\sermon.txt", 'r')
skinchanneltext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\channeltext.txt", 'r')
skinemojitext =  open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\emoji.txt", 'r')
skinemojilisttext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\emojilist.txt", 'r')
skinedgytext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\edgy.txt", 'r')
skineventtext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\events.txt", 'r')
skingrouptext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\groups.txt", 'r')
skinloretext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\lore.txt", 'r')
skinstafftext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\staff.txt", 'r')
skinshiptext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\shipping.txt", 'r')
skinsubunitstext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\subunit.txt", 'r')
skinwordstext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\words.txt", 'r')
skinmainpagetext = open("\\Users\Gabe\PycharmProjects\SpecordWiki\TextFiles\mainpage.txt", 'r')

#getting into categories
def Categories():
    #Goes into Categories
    driver.get('https://specord.fandom.com/wiki/Special:Categories')

#what happens within an article
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

#reading the text files
def OutputSkinFileCharacter():
    #Reads the skin character text file and pastes it
    act = ActionChains(driver)
    skin = skincharactertext.read()
    act.send_keys(skin)
    act.perform()
    skincharactertext.seek(0)
def OutputAloisText():
    #Alois's Page
    act = ActionChains(driver)
    skin = aloistext.read()
    act.send_keys(skin)
    act.perform()
    aloistext.seek(0)
def OutputSoftText():
    act = ActionChains(driver)
    skin = softtext.read()
    act.send_keys(skin)
    act.perform()
    softtext.seek(0)
def OutputBenSermon():
    # Reads the skin character text file and pastes it
    act = ActionChains(driver)
    skin = bensermon.read()
    act.send_keys(skin)
    act.perform()
    bensermon.seek(0)
def OutputSkinFileChannel():
    #Reads the skin channel text file and pastes it
    act = ActionChains(driver)
    skin = skinchanneltext.read()
    act.send_keys(skin)
    act.perform()
    skinchanneltext.seek(0)
def OutputSkinFileEdgy():
    act = ActionChains(driver)
    skin = skinedgytext.read()
    act.send_keys(skin)
    act.perform()
    skinedgytext.seek(0)
def OutputSkinFileEmoji():
    act = ActionChains(driver)
    skin = skinemojitext.read()
    act.send_keys(skin)
    act.perform()
    skinemojitext.seek(0)
def OutputSkinFileEvent():
    act = ActionChains(driver)
    skin = skineventtext
    act.send_keys(skin)
    act.perform()
    skineventtext.seek(0)
def OutputSkinFileGroup():
    act = ActionChains(driver)
    skin = skingrouptext
    act.send_keys(skin)
    act.perform()
    skingrouptext.seek(0)
def OutputSkinFileLore():
    act = ActionChains(driver)
    skin = skinloretext
    act.send_keys(skin)
    act.perform()
    skinloretext.seek(0)
def OutputSkinFileShipping():
    act = ActionChains(driver)
    skin = skinshiptext
    act.send_keys(skin)
    act.perform()
    skinshiptext.seek(0)
def OutputSkinFileEmojiList():
    act = ActionChains(driver)
    skin = skinemojilisttext.read()
    act.send_keys(skin)
    act.perform()
    skinemojilisttext.seek(0)
def OutputSkinFileSpecordStaff():
    act = ActionChains(driver)
    skin = skinstafftext
    act.send_keys(skin)
    act.perform()
    skinstafftext.seek(0)
def OutputSkinFileSubunits():
    act = ActionChains(driver)
    skin = skinsubunitstext
    act.send_keys(skin)
    act.perform()
    skinsubunitstext.seek(0)
def OutputSkinFileWords():
    act = ActionChains(driver)
    skin = skinwordstext
    act.send_keys(skin)
    act.perform()
    skinwordstext.seek(0)

#editing the source code and outputting the text files
def SkinCharacter():
    #Use this function for a character/member
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileCharacter()
    time.sleep(1)
    SavePage()
def BenSermonPage():
    #Use this function for Ben Lee's sermon's page
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputBenSermon()
    time.sleep(1)
    SavePage()
def AloisPage():
    #Use this function for Alois's page
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputAloisText()
    time.sleep(1)

    SavePage()
def EmojiListPage():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileEmojiList()
    time.sleep(1)

    SavePage()
def SoftPage():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSoftText()
    time.sleep(1)

    SavePage()
def SkinChannel():
    #use this for a specific channel's page
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileChannel()
    time.sleep(1)

    SavePage()
def SkinEdgy():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileEdgy()
    time.sleep(1)

    SavePage()
def SkinEmoji():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileEmoji()
    time.sleep(1)

    SavePage()
def SkinEvent():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileEvent()
    time.sleep(1)

    SavePage()
def SkinGroup():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileGroup()
    time.sleep(1)

    SavePage()
def SkinLore():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileLore()
    time.sleep(1)

    SavePage()
def SkinShipping():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileShipping()
    time.sleep(1)

    SavePage()
def SkinSpecordStaff():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileSpecordStaff()
    time.sleep(1)
    SavePage()
def SkinSubunits():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileSubunits()
    time.sleep(1)
    SavePage()
def SkinWords():
    time.sleep(1)
    EditButton()
    time.sleep(2)
    DeleteAll()
    OutputSkinFileWords()
    time.sleep(1)
    SavePage()

#all links
def MainPage():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Specord_Wiki')
    SkinMainPage()
def Aeiriter():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Aeiriter')
    SkinCharacter()
def AK():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/AK')
    SkinCharacter()
def Alois():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Alois')
    AloisPage()
def Ally():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ally')
    SkinCharacter()
def Amarillo():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Amarillo_del_Bosque_Verde')
    SkinCharacter()
def Ambient():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ambient')
    SkinCharacter()
def Ash():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ash')
    SkinCharacter()
def BenLee():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ben_Lee')
    SkinCharacter()
def Black():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Black')
    SkinCharacter()
def Blue():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Blue')
    SkinCharacter()
def Bots():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Bots')
    SkinCharacter()
def Bullying():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Bullying')
    SkinCharacter()
def Caddy():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Caddy')
    SkinCharacter()
def Cass():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Cass')
    SkinCharacter()
def ChaseKip():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Chase_Kip')
    SkinCharacter()
def Copper():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Copper')
    SkinCharacter()
def Crazed():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Crazed')
    SkinCharacter()
def Crt():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Crt')
    SkinCharacter()
def Crystal():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Crystal')
    SkinCharacter()
def Deimos():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Deimos')
    SkinCharacter()
def Ditty():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ditty')
    SkinCharacter()
def Ebra():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ebra')
    SkinCharacter()
def Eeveechu():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Eeveechu')
    SkinCharacter()
def Eggman():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Eggman')
    SkinCharacter()
def Exvnir():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Exvnir')
    SkinCharacter()
def Falco():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Falco')
    SkinCharacter()
def Faust():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Faust')
    SkinCharacter()
def Ghay():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ghay')
    SkinCharacter()
def Ghfrc():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ghfrc')
    SkinCharacter()
def Gibby():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Gibby')
    SkinCharacter()
def Gold():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Gold')
    SkinCharacter()
def GP():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/GP')
    SkinCharacter()
def Green():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Green')
    SkinCharacter()
def Gresh():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Gresh')
    SkinCharacter()
def Hanamits():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Hanamits')
    SkinCharacter()
def Heartman():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/HeartMan')
    SkinCharacter()
def Kusaka():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Hidenori_Kusaka')
    SkinCharacter()
def Jautts():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Jautts')
    SkinCharacter()
def Kris():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Joe_Cool')
    SkinCharacter()
def Jolthicc():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Jolthicc')
    SkinCharacter()
def Khun():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Khun')
    SkinCharacter()
def Lack():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Lacktwo')
    SkinCharacter()
def Leaf():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Leaf')
    SkinCharacter()
def MeTwo():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Me-Two')
    SkinCharacter()
def Mel():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Mel')
    SkinCharacter()
def Mha():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Mha28')
    SkinCharacter()
def Moni():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Moni')
    SkinCharacter()
def Moon():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Moon')
    SkinCharacter()
def Neris():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Neris')
    SkinCharacter()
def Nicole():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Nicole')
    SkinCharacter()
def NightRiley():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/NightRiley')
    SkinCharacter()
def Nobadi():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Nobadi')
    SkinCharacter()
def NobadiAllegedly():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Nobadi_(Allegedly)')
    SkinCharacter()
def Ozzie():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ozzie')
    SkinCharacter()
def Pearl():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Pearl')
    SkinCharacter()
def Pebboe():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Pebboe')
    SkinCharacter()
def PebboeTom():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Pebboe_and_Tom')
    SkinCharacter()
def Piplup():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Piplup')
    SkinCharacter()
def Plantsuke():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Plantsuke_/_Deyvan_Salez')
    SkinCharacter()
def Qami():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Qami')
    SkinCharacter()
def Quip():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Quip')
    SkinCharacter()
def Rebooted():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Rebooted')
    SkinCharacter()
def Red():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Red')
    SkinCharacter()
def Rei():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Rei')
    SkinCharacter()
def Rico():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Rico')
    SkinCharacter()
def Rile():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Rile')
    SkinCharacter()
def Rita():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Rita')
    SkinCharacter()
def Ruby():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ruby')
    SkinCharacter()
def Selphie():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Selphie')
    SkinCharacter()
def Shadow():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Shadow')
    SkinCharacter()
def Shaun():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Shaunathan')
    SkinCharacter()
def Silver():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Silver')
    SkinCharacter()
def Sof():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Sof')
    SkinCharacter()
def Soft():
    time.sleep(1)
    driver.get('/https://specord.fandom.com/wiki/Soft_(softie/softo)')
    SoftPage()
def Soup():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Soup')
    SkinCharacter()
def Spora():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Sporadic')
    SkinCharacter()
def Straw():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Straw')
    SkinCharacter()
def Sun():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Sun')
    SkinCharacter()
def Specordion():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Specordion')
    SkinCharacter()
def Supporter():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Supporter')
    SkinCharacter()
def TomNook():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Tom_Nook')
    SkinCharacter()
def White():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/White')
    SkinCharacter()
def BenSermon():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ben_Lee%27s_Final_Sermon')
    ClickToEndSpecordWiki.BenSermonPage()
def ArtDiscussion():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Art-discussion')
    SkinChannel()
def BotChat():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Bot-chat')
    SkinChannel()
def FE():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Fe3h-discussion')
    SkinChannel()
def FreeChat():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Free-chat')
    SkinChannel()
def Gameverse():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Gameverse')
    SkinChannel()
def General():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/General')
    SkinChannel()
def HallOfShame():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Hall_of_Shame')
    SkinChannel()
def MangaChat():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Manga-chat')
    SkinChannel()
def NSFW():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/NSFW-YAOI')
    SkinChannel()
def Shipping():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Shipping_Chat')
    SkinChannel()
def VC():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/VC')
    SkinChannel()
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
def Bunblush():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Bunblush:')
    SkinEmoji()
def ListOfEmojis():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/List_of_Emojis_in_Specord')
    EmojiListPage()
def ScreenShot():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Screen_Shot_2019-06-18_at_2.31.18_AM')
    SkinEmoji()
def Yeah():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Yeah_(:yeah:)')
    SkinEmoji()
def YellowD():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/YellowD:')
    SkinEmoji()
def EventDiscussionMassacre():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/August_22nd_Event-Discussion_Massacre')
    SkinEvent()
def DiscordMigration():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Discord_Migration_of_2016')
    SkinEvent()
def MCM():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/MCMessenger_ARG')
    SkinEvent()
def Gala():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Special_Gala_Event')
    SkinEvent()
def SpongebobHelps():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Spongebob_helps_Genji_with_his_math_homework')
    SkinEvent()
def BotChatPurge():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Bot-Chat_Purge')
    SkinEvent()
def MeetingOfMinds():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/The_Meeting_of_Minds')
    SkinEvent()
def Clowns():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Clowns')
    SkinGroup()
def LordsOfSpecord():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Lords_of_Specord')
    SkinGroup()
def Specord():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Specord')
    SkinLore()
def Agency():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/AgencyShipping')
    SkinShipping()
def Chosen():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/ChosenShipping')
    SkinShipping()
def EmoOrange():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/EmoOrangeShipping')
    SkinShipping()
def Frantic():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/FRANTICSHITTING')
    SkinShipping()
def Laverre():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/LaverreShipping')
    SkinShipping()
def OldRival():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/OldRivalShipping')
    SkinShipping()
def PreciousMetal():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/PreciousMetalShipping')
    SkinShipping()
def SimilarToSeddie():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Ships_Similar_To_Seddie')
    SkinShipping()
def Special():
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/SpecialShipping')
    SkinShipping()
def SpecordStaff():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Specord_Staff')
    SkinSpecordStaff()
def DottoSquad():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Dotto_Squad')
    SkinSubunits()
def Twenty17Gang():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/2017_Gang')
    SkinSubunits()
def FebruaryGang():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/February_Gang')
    SkinSubunits()
def Hot():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Hot')
    SkinWords()
def Normal():
    # Goes into a specific article
    time.sleep(1)
    driver.get('https://specord.fandom.com/wiki/Normal')
    SkinWords()

#functions
def Characters():
#one by one, they all fall down
   Aeiriter()
   AK()
   Ally()
   Amarillo()
   Ambient()
   Ash()
   BenLee()
   Blue()
   Black()
   Bullying()
   Bots()
   Caddy()
   Cass()
   ChaseKip()
   Copper()
   Crazed()
   Crt()
   Crystal()
   Deimos()
   Ditty()
   Ebra()
   Eeveechu()
   Eggman()
   Exvnir()
   Falco()
   Faust()
   Ghay()
   Ghfrc()
   Gibby()
   Gold()
   GP()
   Green()
   Gresh()
   Hanamits()
   Heartman()
   Kusaka()
   Jautts()
   Kris()
   Jolthicc()
   Khun()
   Lack()
   Leaf()
   MeTwo()
   Mel()
   Mha()
   Moni()
   Moon()
   Neris()
   Nicole()
   NightRiley()
   Nobadi()
   NobadiAllegedly()
   Ozzie()
   Pearl()
   Pebboe()
   PebboeTom()
   Piplup()
   Plantsuke()
   Qami()
   Quip()
   Rebooted()
   Red()
   Rei()
   Rico()
   Rile()
   Rita()
   Ruby()
   Selphie()
   Shadow()
   Shaun()
   Silver()
   Sof()
   Soft()
   Soup()
   Spora()
   Straw()
   Sun()
   Specordion()
   Supporter()
   TomNook()
   White()
def BlogPosts():
    BenSermon()
def Channels():
    ArtDiscussion()
    BotChat()
    FE()
    FreeChat()
    Gameverse()
    General()
    HallOfShame()
    MangaChat()
    NSFW()
    Shipping()
    VC()
def Edgy():
    SpongebobWelcome()
    PokemonSpecial()
def Emoji():
    Bunblush()
    ListOfEmojis()
    ScreenShot()
    Yeah()
    YellowD()
def Event():
    BotChatPurge()
    DiscordMigration()
    EventDiscussionMassacre()
    Gala()
    MCM()
    MeetingOfMinds()
    SpongebobHelps()
def Group():
    Clowns()
    LordsOfSpecord()
def Lore():
    Specord()
def Shipping():
    Agency()
    Chosen()
    EmoOrange()
    Frantic()
    Laverre()
    OldRival()
    PreciousMetal()
    SimilarToSeddie()
    Special()
def Staff():
    SpecordStaff()
def Subunits():
    SubunitsArticles.DottoSquad()
    SubunitsArticles.FebruaryGang()
    SubunitsArticles.Twenty17Gang()
def Words():
    WordsArticles.Hot()
    WordsArticles.Normal()

def main():
    driver.get("https://specord.fandom.com/wiki/Specord_Wiki")
    time.sleep(25)
    Categories()
    #buffer time, login to burner email edit the main page
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
    Alois()
    time.sleep(40)
    driver.close()


main()