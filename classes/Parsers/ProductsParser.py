from ..Product import Product
import json

class ProductParser:

    file_path = ""
    file_descriptor = None

    def __init__(self, file):
        self.file_path = file

    def Parse(self):
        lines = self.ReadFile()
        products = []
        for line in lines:
            products.append(self.CreateProduct(line))
        return products        

    def ReadFile(self):
        self.file_descriptor = open(self.file_path,"r")
        return self.file_descriptor.readlines()

    def CreateProduct(self, line):
        product_raw = json.loads(line)
        return Product(product_raw['Web'], product_raw['Link'], product_raw['Name'], product_raw['Price'])
