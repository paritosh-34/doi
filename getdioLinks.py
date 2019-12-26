import requests
from bs4 import BeautifulSoup

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }


def doiLinks(url):
    if url.endswith("pdf"):
        return url
    s = requests.Session()
    r = s.get(url, headers=headers_Get, verify=False)
    soup = BeautifulSoup(r.text, "html.parser")
    links_with_text = []
    for a in soup.find_all('a', href=True):
        if a.text:
            links_with_text.append(a['href'])
    matching = [s for s in links_with_text if "doi.org" in s]
    if len(matching) == 0:
        return ""
    return matching[0]


# doiLinks('https://digital.csic.es/handle/10261/196754')