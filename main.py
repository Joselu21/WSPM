from classes.PriceMonitor import PriceMonitor
from classes.WebScraper import WebScraper
from classes.Product import Product
from os.path import isfile, join
from os import listdir
import glob
import sys

def Help():
    print('Web Scraper: Uses a config file to explore a website and extract all products and prices to a file in data/\"Website Name\"/Discovered.txt')
    print('An example of this file can be found in data/web/example.json')
    print('If no configuration file is provided it will execute all configuration files present in data/web/ directory')
    print('Usage: wspm -Ws [web_congig_file]')
    print('')
    print('Price Monitor: Checks if the product\'s price discovered by a previous execution of the Web Scrapper functionality is below a threshold specified by you')
    print('Usage: wspm -Pm [product_file] [user_config]')

def WebScraping(config_file = None):
    if(config_file != None):
        web = WebScraper(config_file)
        web.Search()
    else: 
        config_files = [f for f in listdir("data/web/") if isfile(join("data/web/", f))]
        for config_file in config_files:
            web = WebScraper(config_file)
            web.Search()

def PriceMonitoring(product_file = None, user_config = None):
    if(product_file != None):
        monitor = PriceMonitor(product_file, user_config)
        monitor.Check()
    else:
        filenames = []
        for filename in glob.iglob("data/" + '**/*.txt', recursive=True):
            filenames.append(filename)
        monitor = PriceMonitor(filenames, user_config)
        monitor.Check()
        

def main():

    print('Welcome to this web scraper and price monitor made in Python 3.9 by Joselu21')
    print('Don\'t forget to check the github respository for updates that can improve the performance or fix errors' )
    print('https://github.com/Joselu21/WSPM')

    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    if("-h" in opts):
        Help()
    elif ("-Ws" in opts):
        arg_index = sys.argv.index("-Ws") + 1
        if(len(sys.argv) - arg_index > 0):
            WebScraping(sys.argv[arg_index])
        else:
            print('Invalid call format, please read the help below \n')
            Help()
    elif ("-Pm" in opts):
        product_index = sys.argv.index("-Pm") + 1
        user_index = sys.argv.index("-Pm") + 2
        if(len(sys.argv) - user_index > 0):
            PriceMonitoring(sys.argv[product_index], sys.argv[user_index])
        elif(len(sys.argv) - product_index > 0):
            PriceMonitoring(sys.argv[product_index])
        else:
            print('Invalid call format, please read the help below \n')
            Help()
    else:
        Help()


if(__name__ == "__main__"):
    main()