import selenium
from .SeleniumController import Selenium

class Product:

    link = ""
    web = ""
    name = ""
    price = 0

    def __init__(self, web, link, name = "", price = 0):
        self.web = web
        self.link = link
        self.name = name
        self.price = price
        if(self.name == "" or self.price == 0):
            self.ExtractData()

    def ExtractData(self):
        searcher = Selenium(self.link)
        searcher.OpenUrl(4)
        array = searcher.ExtractProductData()
        self.name = array[0]
        self.price = float(array[1])
        searcher.Quit()

    def To_String(self):
        return "{{ \"Web\": \"{}\", \"Name\": \"{}\", \"Link\": \"{}\", \"Price\": {} }} \n".format(self.web, self.name, self.link, self.price)


