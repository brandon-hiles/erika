__version__ = 0.3
__author__ = "Brandon Hiles"

import requests
import nltk
import re
import bs4
import xml
import zlib
import threading
from queue import Queue

from src.api.db.mongo import Mongo # Import Mongo Database Module

class Worker(threading.Thread):

    """
    Worker object that will be responsible for extracting
    each individual sitemap xml file.
    """

    def __init__(self, queue, website, host, port, collection):
        threading.Thread.__init__(self)
        self.queue = queue
        self.website = website
        self.host =  host
        self.port = port
        self.collection = collection
        self.database = "news"
        self.parser = SiteMapParser(website=self.website, host = self.host, port=self.port, collection=self.collection)
        self.mongo = Mongo(host=self.host, port=self.port, database="news")

    def run(self):
        vals = []
        while True:
            url = self.queue.get()
            try:
                data = self.parser.grab_data(url)
                sites = self.parser.parse_sitemap_data(data=data)[1]
                website = self.parser.get_websites(sites=sites)

                collect = self.mongo.select_database(self.database)[self.collection + '_urls']
                for data in website:
                    collect.insert_one({"url" : data}).inserted_id
            finally:
                self.queue.task_done()
        return vals

class SiteMapParser(object):

    """
    SiteMapParser is the main base class for parsing economic
    news sites.

    Description: SiteMapParser utilizes the robots.txt file provided
    by the news sites to crawl through the available sitemap data.
    Initialization:
    1. website: Provide a website that you want crawl though and collect
    data
    2. host:
    """

    def __init__(self, website, host, port, collection):
        self.website = website
        self.host = host
        self.port = port
        self.database = "news"
        self.collection = collection
        self.mongo = Mongo(host=self.host, port=self.port, database=self.database)
        self.threads = 0 # Define the number of threads needed

    def grab_elements(self, website):
        # This extracts the Tag class from html page
        # Note: This needs an html page, NOT a url.

        soup = bs4.BeautifulSoup(website, 'html.parser')
        children = list(soup.children)
        element = [children[num] for num, value in enumerate(children)
        if type(children[num]) is bs4.element.Tag]
        return element

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
            self.threads = len(sites) # Define the number of threads needed
        except requests.ConnectionError:
            print("Website does not have a robots.txt file")

        return sites

    def grab_data(self, url):

        #print("Starting Thread")
        web_data = requests.get(url).content
        xml_str = ".xml.gz"
        data = ''
        if xml_str in url:
            decompressed_data =  zlib.decompress(web_data, 16+zlib.MAX_WBITS)
            data = decompressed_data
        else:
            data = web_data
        #print("Ending Thread")
        return data

    def parse_sitemap_data(self, data):

        sites = []
        errors = []
        try:
            root = xml.etree.ElementTree.fromstring(data)
            for index in range(0, len(root)):
                sites.append(root[index][0].text)
        except xml.etree.ElementTree.ParseError:
            errors.append(num)

        return len(errors), sites

    def parse_data(self, data):

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
                        #print(root[index][0].text)
                else:
                    root = xml.etree.ElementTree.fromstring(site)
                    for index in range(0, len(root)):
                        sites.append(root[index][0].text)
                        #print(root[index][0].text)
            except xml.etree.ElementTree.ParseError:
                errors.append(num) # Container counting amount of errors
                continue

        return len(errors), sites

    def get_websites(self, sites):

        data = self.parse_data(data=sites)[1]
        urls = []
        for num, value in enumerate(data):
            if len(self.mongo.check_database_by_url(collection=self.collection, url=data[num])) == 1: # Data is in database
                print("NOT ADDING TO LIST")
                pass
            else: # data is not in database
                print(data[num])
                urls.append(data[num])
        return urls

    def main(self):

        # Create a queue to communicate with the worker threads
        queue = Queue()
        links = self.grab_sitemap_urls()
        data = []
        for num in links:
            worker = Worker(queue, website=self.website, host=self.host, port=self.port, collection=self.collection)
            # Setting daemon to True will let the main thread exist even though the works are blocking
            worker.daemon = True
            data.append(worker.start())
        for link in links:
            print("Queueing")
            queue.put(link)
        queue.join()
        print("----------------------------------")
        print(data)
        print("Done")
