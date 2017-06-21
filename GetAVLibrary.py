# -- coding: utf-8 --
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"}
url_avLibrary = 'http://www.j12lib.com/cn/'

def getInfoFromName(starName):
    sess = requests.Session()
    url_avStar = '{}/vl_star.php?s={}'.format(url_avLibrary,starName)
    r = sess.get(url_avStar, headers=headers).text
    pageCount = BeautifulSoup(r, 'lxml').find('div', class_="page_selector").find('a',class_='page last').get('href').split('=')[-1]
    urls = [url_avLibrary+'/vl_star.php?&mode=&s='+starName+'&page='+str(i+1) for i in range(int(pageCount))]
    productUrls = []
    for i, url in enumerate(urls):
        r = sess.get(url, headers=headers).text
        detailPages = BeautifulSoup(r,'lxml').find('div', class_='videothumblist').find('div',class_='videos').findAll('div', class_='video')
        for tmp in detailPages:
            detailPageKey = tmp.get('id').split('_')[-1]
            detailPage = url_avLibrary + '?v=' + detailPageKey
            getInfoFromProduct(sess, detailPage)
            productUrls.append(detailPage)

    print productUrls
def getInfoFromProduct(sess, url):
    r = sess.get(url, headers=headers).text
    labelTags = BeautifulSoup(r,'lxml').find('div', id='video_genres').findAll('span',class_='genre')
    labels = []
    tmpFile = open('tmp.txt','a')
    tmpFile.write(url+'\n')
    #print url
    for tmp in labelTags:
        label = tmp.get_text()
        #print label
        tmpFile.write(label+' ')
        labels.append(label)
    tmpFile.write('\n')
getInfoFromName('azlcq')