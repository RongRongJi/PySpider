from bs4 import BeautifulSoup
import requests
import time
from Spider.SpiderProxy import SpiderProxy as sp


class SpiderTemplate:

    #初始化网页信息
    def __init__(self, header, url):
        self.headers=header
        self.url=url
        self.proxy={}
        spiderproxy = sp()
        list = spiderproxy.GetProxyList()
        for i in range(len(list)):
            self.proxy.update({'http':list[i]})

    # 设置代理
    def setProxy(self,proxy):
        self.proxy=proxy

    #爬取页面信息
    def spider(self):
        #time.sleep(2)
        response = requests.get(url=self.url,headers=self.headers,proxies=self.proxy)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        return soup

