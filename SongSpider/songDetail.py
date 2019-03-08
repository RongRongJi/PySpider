import Spider.spider as s
import threading
import time


class MusicDetail:
    def __init__(self,songs):
        self.tags=songs[0]
        self.urls=songs[1]
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.detials=[]

    def getSongAndSinger(self,url):
        songurl = 'https://music.163.com' + url
        spider = s.SpiderTemplate(header=self.headers, url=songurl)
        soup = spider.spider()
        #获取歌名
        title = soup.select('.f-ff2')[0].get_text()
        #获取歌手信息
        singer = soup.select('.des')[1].get_text()
        #获取专辑信息
        album = soup.select('.des')[2].get_text()
        print(self.tags,title,singer,album)
        return {'tags':self.tags, 'title':title, 'singer':singer, 'album':album}

    def startSpider(self):
        details = []
        for i in range(0,len(self.urls)):
            details.append(self.getSongAndSinger(self.urls[i]))
        return details



