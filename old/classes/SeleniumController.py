from re import search
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import configparser as ConfigParser
import time

class Selenium:

    driver = None
    search_page = ""
    product_xpath = ""
    cookies_xpath = ""

    def __init__(self, search_page = "", product_xpath = "", cookies_xpath = ""):
        configparser = ConfigParser.RawConfigParser()
        configFilePath = 'config.ini'
        configparser.read(configFilePath)
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
        #options.add_argument('--start-maximized')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(configparser.get('SELENIUM', 'chromedriver_path'), options=options)
        self.search_page = search_page
        self.product_xpath = product_xpath
        self.cookies_xpath = cookies_xpath

    def SearchForProducts(self):
        elements = self.driver.find_elements_by_xpath(self.product_xpath)
        return elements

    def OpenUrl(self, seconds = 1):
        self.driver.get(self.search_page)
        self.ClearCookies()
        time.sleep(seconds)

    def AcceptCookies(self, seconds = 1, attempts = 10):     
        try:
            cookies = self.driver.find_element_by_xpath(self.cookies_xpath)
            action = ActionChains(self.driver)
            action.click(cookies).perform()
            time.sleep(seconds)
        except:
            time.sleep(seconds)
            if(attempts <= 0):
                return
            self.AcceptCookies(seconds, attempts - 1)

    def ViewMore(self, buttonId = "btnMore", seconds = 1):
        self.ClearCookies()
        self.ScrollDownSmoothlyUntilID(buttonId, True)
        self.ClearCookies()
        time.sleep(seconds)

    def ScrollDownSmoothlyUntilID(self, id = None, click = False, seconds = 0.1):
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        for i in range(1, total_height, 100):
            self.driver.execute_script("window.scrollTo(0, {});".format(i))
            total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
            time.sleep(seconds)
            if(id != None and self.driver.find_element_by_id(id).is_displayed()):
                if click:
                    self.Click(id)
                return

    def ScrollDownSmoothlyWhileProducts(self, seconds = 0.1):
        offsetY = self.driver.execute_script("return window.pageYOffset;")
        total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
        
        while offsetY < total_height:
            offsetY += 200
            self.driver.execute_script("window.scrollTo(0, {});".format(offsetY))
            total_height = int(self.driver.execute_script("return document.body.scrollHeight"))
            time.sleep(seconds)

    def Click(self, id):
        button = self.driver.find_element_by_id(id)
        action = ActionChains(self.driver)
        action.click(button).perform()

    def ClearCookies(self):
        self.driver.delete_all_cookies()

    def ExtractProductData(self):
        price = self.driver.find_element_by_id('precio-main').get_attribute('data-price')
        name = self.driver.find_element_by_xpath("//*[@id=\"contenedor-principal\"]/div/div/div/div/div/div/h1/strong").text
        return [name, price]

    def Quit(self):
        self.driver.quit()
