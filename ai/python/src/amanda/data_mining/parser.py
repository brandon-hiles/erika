__version__ = 0.2
__author__ = "Brandon Hiles"

import requests
import nltk
import re
import bs4
import xml
import zlib

class SiteMapParser(object):

    """
    SiteMapParser is the main base class for parsing economic
    news sites.

    Description: SiteMapParser utilizes the robots.txt file provided
    by the news sites to crawl through the available sitemap data.
    Initialization: 
    1. website: Provide a website that you want crawl though and collect
    data
    """

    def __init__(self, website):
        self.website = website

    def grab_sitemap_urls(self):

        try:
            web_data = requests.get(self.website + '/robots.txt'
                ).content.decode("utf-8")
            tokenizer = nltk.tokenize.TreebankWordTokenizer()
            temp_data = tokenizer.tokenize(web_data)
            sites = ['https://' + temp_data.strip("//") 
            for temp_data in temp_data if "//" in temp_data]
            # sites retrieves all sites, and we need to filter
            # this list to look for only sitemap websites.
            filter = ['sitemap']
            sites = [sent for sent in sites
                if any(word in sent for word in filter)]
        except requests.ConnectionError:
            print("Website does not have a robots.txt file")

        return sites

    def grab_data(self):

        urls = self.grab_sitemap_urls()
        data = [[] for url in urls]
        for value, url in enumerate(urls):
            web_data = requests.get(url).content
            string = ".xml.gz"
            if string in url:
                decompressed_data = zlib.decompress(web_data, 16+zlib.MAX_WBITS)
                data[value].append(decompressed_data)
            else:
                data[value].append(web_data)
        return data

    def grab_websites(self):
        
        errors, data = self.parse_sitemap_data()

        sitemapData = []
        for num,value in enumerate(data):
            sitemapData.append(data[num])
        return sitemapData

    def grab_elements(self, website):
        # This extracts the Tag class from html page

        soup = bs4.BeautifulSoup(website, 'html.parser')
        children = list(soup.children)
        element = [children[num] for num, value in enumerate(children) 
        if type(children[num]) is bs4.element.Tag]
        return element

    def parse_sitemap_data(self):

        data = self.grab_data()
        sites = []
        errors = []
        for url, num in enumerate(data):
            try:
                temp = data[url][0]
                root = xml.etree.ElementTree.fromstring(temp)
                for index in range(0, len(root)):
                    sites.append(root[index][0].text)
            except xml.etree.ElementTree.ParseError:
                errors.append(num)
                continue

        return len(errors), sites

    def parse_data(self, data):

        # We need to add threading to this method

        errors = []
        sites = []
        for num, val in enumerate(data):
            try:
                site = requests.get(data[num]).content
                string = ".xml.gz"
                if string in data[num]:
                    decompressed_data = zlib.decompress(site, 16+zlib.MAX_WBITS)
                    root = xml.etree.ElementTree.fromstring(decompressed_data)
                    for index in range(0, len(root)):
                        sites.append(root[index][0].text)
                        print(root[index][0].text)
                else:
                    root = xml.etree.ElementTree.fromstring(site)
                    for index in range(0, len(root)):
                        sites.append(root[index][0].text)
            except xml.etree.ElementTree.ParseError:
                errors.append(num) # Container counting amount of errors
                continue

        return len(errors), sites

    def get_websites(self):

        sitemaps = self.grab_websites()
        data = self.parse_data(data=sitemaps)[1]
        urls = []
        for num, value in enumerate(data):
            print(num)
            urls.append(data[num])
        return urls