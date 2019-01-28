__version__ = 0.2
__author__ = "Brandon Hiles"

import bs4
import re
import requests
from pymongo import MongoClient

from src.api.db.mongo import Mongo
from src.api.data_mining.parser import SiteMapParser

class Reuters(SiteMapParser):

    """
    Reuters is an interface for parsing data from reuters.com

    Initialization Parameters:
    1. Host: Default parm: localhost
    2. Port: Used to specify the port instance of the db
       Default Parm: 27017
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.db = "news"
        self.mongo = Mongo(host=self.host, port=self.port)
        super().__init__(website='https://www.reuters.com')

    def _extract_text(self, website):
        # Extracts article from html page

        element = super().grab_elements(website)
        text = element[0].find_all("p")
        text = [''.join(text[num].text) for num, val in enumerate(text)]
        text = "".join(text)
        return text

    def _extract_title(self, website):
        # Extracts the title from the html page

        element = super().grab_elements(website)
        title = element[0].find("title").text

        # Clean up text section
        title = re.sub(' +', ' ', title)
        title = title.split("|")[0] # Since title contains | Reuters, we split it.
        title = title.replace("\n", "")
        return title

    def _extract_tags(self, website):
        # Extracts tags via the <meta> section

        element = super().grab_elements(website)
        tag = element[0].find("meta",  property="og:article:tag")
        if type(tag) is bs4.element.Tag:
            return tag['content']
        if type(tag) is  None:
            return ""

    def _extract_authors(self, website):
        # Extracts authors of the text via <meta> section

        element = super().grab_elements(website)
        author = element[0].find("meta",  property="og:article:author")
        if type(author) is bs4.element.Tag:
            return author['content']
        if type(author) is None:
            return ""

    def store_websites(self, upper_bound):

        client = self.mongo.client()
        db = client['news']
        reuters = db['reuters']

        urls = super().get_websites()

        for index in range(0, upper_bound+1):
            website = requests.get(urls[index]).content.decode('utf-8')
            query = { 
                "title" : self._extract_title(website),
                "article" : self._extract_text(website),
                "authors" : self._extract_authors(website),
                "meta" : {
                    "url" : urls[index],
                    "tags" : self._extract_tags(website)
                    }
                }
            check_query = {"title" : self._extract_title(website)}
            check = self.mongo.check_collection(db=self.db, collection='reuters',query=check_query)
            if check == False: # Checks that doesn't already exist in db
                reuters.insert_one(query).inserted_id

    def url_type(self, url):
        # There are 2 types of urls presented in sitemap data:
        # 1. Articles
        # 2. Videos
        # This method is used for sorting in database for CV vs. NLP 
        # distinstion

        if url.split('/')[3] == 'article':
            return 'article'
        elif url.split('/')[3] == 'videos':
            return 'videos'