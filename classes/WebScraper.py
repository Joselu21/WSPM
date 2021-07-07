import os
from classes.Product import Product
from .SeleniumController import Selenium
from .Product import Product

class WebScraper:

    web_name = "pccomponentes.com"
    search_page = "https://www.pccomponentes.com/tarjetas-graficas"
    xpath = "//*[@id=\"articleListContent\"]/div/div/article/div/a"
    products = []

    def __init__(self, config) -> None:
        pass

    def Search(self):
        searcher = Selenium(self.search_page, self.xpath, "//*[@id=\"familia-secundaria\"]/div[6]/div/div/div[2]/button")
        searcher.OpenUrl(seconds=0) 
        searcher.AcceptCookies()
        searcher.ViewMore(seconds=0)
        searcher.ScrollDownSmoothlyWhileProducts()
        product_lines = searcher.SearchForProducts()
        links = self.GetLinks(product_lines)
        searcher.Quit()
        self.CreateProducts(product_lines, links)
        self.Save()
    
    def CreateProducts(self, list, links):
        for i  in range(0, len(list)):
            self.products.append(Product("https://" + self.web_name, links[i]))
        
    def GetLinks(self, product_lines):
        links = []
        for product_line in product_lines:
            links.append(product_line.get_attribute('href'))
        return links

    def Save(self):
        if(not os.path.isdir("data/product/{}/".format(self.web_name))): 
            os.mkdir("data/product/{}/".format(self.web_name))
        file = open(r"data/product/{}/Discovered.json".format(self.web_name),"w")
        for product in self.products:
            file.write(product.To_String())
        file.close()
