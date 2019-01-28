from pymongo import MongoClient

class Mongo(object):

    def __init__(self, host, port):
	    self.host = host
	    self.port = port

    def client(self):
	    return MongoClient(self.host, self.port)

    def find(self, query):
        # Find item in mongoDB given a query
        client = self.client()
        db = client['news']
        reuters = db['reuters']
        result = reuters.find_one(query)
        title = result['title']
        article = result['article']
        authors = result['authors']
        url = result['meta']['url']
        tags = result['meta']['tags']

        return title, article, authors, url, tags

    def database_headers(self):
        # Some html to help verify info. (Once frontend is complete, this function will be deleted)
        return '<tr> Title </tr> <tr> Article </tr> <tr> Authors </tr> <tr> Url </tr> <tr> Tags </tr>'

    def generate_table_html(self, query):

        # Makes a query to db and returns data in table format
        
        title, article, authors, url, tags = self.find(query=query)
        table_html_open = '<table style="width:100%">'
        headers = self.database_headers()
        data = f'<td> {title} </td> <td> {article} </td> <td> {authors} </td> <td> {url} </td> <td> {tags} </td>'
        table_html_close = '</table>'
        html = table_html_open + headers + data + table_html_close
        return html