import requests
from bs4 import BeautifulSoup

sess = requests.Session()
url_CaoLiu = 'http://owxxww.com/index.php/'
#url_JiShuTaoLun = url_CaoLiu+'thread0806.php?fid=7'
url_JiShuTaoLun = 'http://owxxww.com/thread0806.php?fid=7'
payload = {'search':'','page':'1'}
r = sess.get(url_JiShuTaoLun)
soup = BeautifulSoup(r.content,"html.parser",from_encoding="gb18030")
#print soup
#soupContent = soup.prettify().encode('utf-8')
#print soupContent
for lineContent in soup.findAll('tr',align="center",class_="tr3 t_one"):
    #print lineContent
    htmlPath = lineContent.find('td').findNext('a')
    #print htmlPath.get('href')
    HTML_PATH = htmlPath.get('href')
    for title in lineContent.findAll('h3'):
        TITLE = title.string
        print title.string
    for readNumber in lineContent.findAll('td',class_="tal f10 y-style"):
        READ_NUMBER = readNumber.string
        #print readNumber.string
    print TITLE, READ_NUMBER

