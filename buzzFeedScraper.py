""" Scrapes the tiles from an html page containing a list of BuzzFeed articles """
from lxml import etree
from io import StringIO, BytesIO

class Scraper:
    def __init__(self):
        pass

    def getFile(self, page):
        """Gets the data from an html file and stores it as a string"""
        with open(page) as f:
            data = f.read()
            # print(data) # is a str object
        # tree = etree.fromstring(data)
        parser = etree.HTMLParser()
        tree = etree.parse(StringIO(data), parser)
        # result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
        return tree

    def getTitles(self, htmlTree):
        titles = []
        for elem in htmlTree.xpath('//*[@id="page_container"]/div/div[4]/ul/li'):
            for link in elem:
                titles.append(link.text)
        return titles



if __name__ == '__main__':
    scraper = Scraper()
    tree = scraper.getFile('buzzfeed-archive-2014/01/01.html')

    print(scraper.getTitles(tree))
