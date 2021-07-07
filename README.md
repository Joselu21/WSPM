# WSPM
Web Scraper and Price Monitor (WSPM) is a useful tool made in Python with Selenium that is prepared to scrap webshops with configurable patterns in json format, and can track the prices of the scrapped products. You can configure users to be notified by email when certain products, especified by patterns (e.g RTX 3060 Ti) are below a threshold price 

## Web Scraping


## Price Monitor

A Price Monitor is a tool that automates the search of prices updates for products of your choice.

This tool can run with several modes, as long as the configuration needed for each one is satisfied.

### Update a list of products previously scrapped

If you want to update prices for a list of products, but have other lists that will slow down the process or don't want to update, this is your choice.
You can use the following command:
```perl
$ python main.py -Pm data/product/website/Discovered.json
```
the program will evaluate all the products inside Discovered.json, updating their name (because products of a link may vary) and price.

### Update all products scrapped

You can omit the "list_of_products.json" file and the program will work, but all the files inside data/products/ will be evaluated, including subdirectories.
That's a good option if you have few lists or if you really want to update all of them but that's a slow process.

```sh
$ python main.py -Pm all
```

### Update a list of products and notify user




