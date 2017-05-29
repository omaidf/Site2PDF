from __future__ import with_statement
from bs4 import BeautifulSoup
import requests
import pdfkit
import time

def parsepages(pages):
    site = "https://www.cyberciti.biz/faq/page/"
    while pages < 411:
        url = site + str(pages)
        pages +=1
        print url
        getlinks(url)


def getlinks(site):
    r = requests.get(site)
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    title = soup.find_all("h2", class_="entry-title")
    for div in title:
        links = div.find_all('a')
        for a in links:
            makepdf(a['href'])


def makepdf(site):
    print site
    r = requests.get(site)
    data = r.text
    print "request done!"
    soup = BeautifulSoup(data,"lxml")
    title = soup.find_all("h1", class_="entry-title")
    text = soup.find_all("div",class_="entry-content")
    content = str(text[0])
    print "content found"
    contentr = content.decode('utf-8').strip()
    html = """
    %s

    %s
    """ % (title[0],contentr)
    print "html created"
    output = str(time.time()) + ".pdf"
    print "outputting pdf"
    pdfkit.from_string(html, output)


parsepages(1)