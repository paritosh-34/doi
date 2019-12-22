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


def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    # url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'

    output=[]
    for i in range(0, 10):
        url = 'https://scholar.google.com/scholar?start=' + str(i*10) + '&q=' + q + '&ie=utf-8&oe=utf-8&as_sdt=1,5&as_vis=1'
        r = s.get(url, headers=headers_Get)

        soup = BeautifulSoup(r.text, "html.parser")
        for searchWrapper in soup.find_all('h3', {'class': 'gs_rt'}): #this line may change in future based on google's web page structure
            url = searchWrapper.find('a')["href"]
            text = searchWrapper.find('a').text.strip()
            result = {'text': text, 'url': url}
            output.append(result)

    return output


# res = google('apple')
# print(res)