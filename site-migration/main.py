import requests
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

class parseSitemap:
    def __init__(self, url: str):
        self.url = url

    def saveHtml(siteurl, count: int):
        response = urllib.request.urlopen(siteurl)
        webContent = response.read().decode('UTF-8')
        htmlFile = f'atlassian.com{count}.html'
        f = open(htmlFile, 'w')
        f.write(webContent)
        f.close

    def parseSitexml(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'xml')
        urls = soup.find_all('loc')
        count = 0
        for url in urls:
            currentURL = url.get_text()
            parseSitemap.saveHtml(currentURL,count)
            count += 1


parseSitemap.parseSitexml("https://www.atlassian.com/sitemap.xml")






