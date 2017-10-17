""" Scrapes the tiles from an html page containing a list of BuzzFeed articles """
from lxml import etree
from io import StringIO, BytesIO
import os

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
                titles.append(link.text.lower())
        return titles

    # appends the list of titles to the specified file
    # each title becomes a sentence
    def writeOutFile(self, titlesList, writeOutFileName):
        f = open(writeOutFileName, "w")
        for title in titlesList:
            f.write(title + ".\n");
        f.close()

if __name__ == '__main__':
    scraper = Scraper()
    tree = scraper.getFile('buzzfeed-archive-2014/01/01.html')
    titles = scraper.getTitles(tree)
    """
    marx = open('marx.txt', 'r')
    finalFile = open('corpus.txt', 'a+')
    finalFile.write(marx.read())
    marx.close()
    dirString = 'Titles/'
    directory = os.fsencode(dirString)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filepath = (os.path.join(dirString, filename))
        titleFile = open(filepath)
        finalFile.write(titleFile.read())
        titleFile.close()
    finalFile.close()

"""

    dirString = 'buzzfeed-archive-2014/01/'
    directory = os.fsencode(dirString)
    i = 0
    for file in os.listdir(directory):
        i += 1
        filename = os.fsdecode(file)
        if filename.endswith('.html'):
            filepath = (os.path.join(dirString, filename))
            tree = scraper.getFile(filepath)
            titles = scraper.getTitles(tree)
            scraper.writeOutFile(titles, 'titles_' + str(i))




    #
