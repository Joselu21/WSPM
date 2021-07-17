from email.message import EmailMessage
import configparser as ConfigParser
import smtplib, ssl
import json

class UserConfigParser:

    file_path = ""
    file_descriptor = ""

    def __init__(self, user_config):
        if(user_config != None):
            self.file_path = user_config

    def Parse(self):
        if (self.file_path != ""):
            self.file_descriptor = open(self.file_path,"r")
            user_raw = json.load(self.file_descriptor)
            thresholds = self.ExtractThresholds(user_raw)
            return UserInfo(user_raw['name'], user_raw['email'], thresholds)

    def ExtractThresholds(self, user_raw):
        thresholds = []
        for threshold in user_raw['thresholds']:
            thresholds.append(Threshold(threshold['product_name'], int(threshold['price_threshold'])))
        return thresholds


class UserInfo:

    name = "" 
    email = ""
    thresholds = None 
    products_email = []

    def __init__(self, name, email, thresholds):
        self.name = name
        self.email = email
        self.thresholds = thresholds

    def BelowThreshold(self, product):
        for threshold in self.thresholds:
            if(threshold.IsInName(product.name) and threshold.BelowThreshold(product.price)):
                self.products_email.append(product)
        return len(self.products_email) > 0
                    
    def SendEmail(self):
        config =  ConfigParser.RawConfigParser(); config.read('config.ini')
        email = config.get('EMAIL', 'gmail_address')
        password = config.get('EMAIL', 'gmail_password')
        port = 465  # For SSL
        context = ssl.create_default_context() # Create a secure SSL context

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email, password)
            msg = EmailMessage()
            msg['Subject'] = "Hola {}, hay productos que han bajado de precio y te interesan""".format(self.name)
            msg['From'] = email
            msg['To'] = self.email
            msg.set_content(self.ProductsEmailToJson()) 
            server.send_message(msg)
            server.quit()

    def ProductsEmailToJson(self):
        string = ""
        for product in self.products_email:
            string += product.To_String()
            string += "\n"
        return string

class Threshold:

    product_name = []
    threshold_price = 0

    def __init__(self, name, price):
        self.product_name = name
        self.threshold_price = price 

    def BelowThreshold(self, current_price):
        return current_price <= self.threshold_price

    def IsInName(self, product_name):
        for i in self.product_name:
            if i not in product_name:
                return False
        return True