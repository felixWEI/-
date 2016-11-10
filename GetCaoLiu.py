import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    sess = requests.Session()
    url_CaoLiu = 'http://owxxww.com'
    #url_JiShuTaoLun = url_CaoLiu+'thread0806.php?fid=7'
    url_JiShuTaoLun = 'http://owxxww.com/thread0806.php?fid=7'
    #page number
    payload = {'search':'','page':'1'}
    r = sess.get(url_JiShuTaoLun, params=payload)
    soup = BeautifulSoup(r.content,"html.parser",from_encoding="gb18030")
    #print soup
    #soupContent = soup.prettify().encode('utf-8')
    #print soupContent
    for lineContent in soup.findAll('tr',align="center",class_="tr3 t_one"):
        #print lineContent
        htmlPath = lineContent.find('td').findNext('a')
        htmlPath = htmlPath.get('href')
        pageUrl = url_CaoLiu+'/'+htmlPath
        for title in lineContent.findAll('h3'):
            pageTitle = title.string
            #print title.string
        for auther in lineContent.findAll('td',class_="tal y-style"):
            auther = auther.find('a').string
            print auther
        for readNumber in lineContent.findAll('td',class_="tal f10 y-style"):
            readNumber = readNumber.string

        print pageTitle, readNumber, auther
        #print pageUrl

