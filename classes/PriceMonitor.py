from .Parsers.ProductsParser import ProductParser
from .Parsers.UserConfigParser import UserConfigParser, UserInfo, Threshold
from .Product import Product

class PriceMonitor:

    products_to_monitor = []
    user_info = None
    
    def __init__(self, products_file, user_file = None):
        self.user_info = UserConfigParser(user_file).Parse()
        self.products_to_monitor = ProductParser(products_file).Parse()

    def Check(self):
        for product in self.products_to_monitor:
            product.ExtractData()
            if(self.user_info != None and self.user_info.BelowThreshold(product)):
                self.user_info.SendEmail()

