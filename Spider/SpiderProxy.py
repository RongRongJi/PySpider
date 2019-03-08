from bs4 import BeautifulSoup
import requests
import urllib
import socket
import lxml


class SpiderProxy:
    proxyList=[]

    def __getProxyIp(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        proxy = []
        for i in range(1, 2):
            try:
                url = 'http://www.xicidaili.com/nn/' + str(i)
                response = requests.get(url=url, headers=header)
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')
                ips = soup.select('.odd')
                for x in range(1, len(ips)):
                    ip = ips[x]
                    tds = ip.findAll("td")
                    ip_temp = tds[1].contents[0] + ":" + tds[2].contents[0]
                    #ip_temp = tds[1].contents[0]
                    proxy.append(ip_temp)
            except:
                continue
        return proxy


    def validateIp(self):
        proxy = self.__getProxyIp()
        #print(proxy)
        url = "http://ip.chinaz.com/"
        socket.setdefaulttimeout(3)
        proxyList = []
        for i in range(0, len(proxy)):
            try:
                proxy_host =  proxy[i]
                proxy_temp = {"http": proxy_host}
                r = requests.get(url,proxy_temp)
                soup = BeautifulSoup(r.text, 'lxml')
                parent_node = soup.find(class_="IpMRig-tit")
                proxyList.append(proxy[i])
                break
            except Exception as err:
                print (err)
                continue
        SpiderProxy.proxyList=proxyList
        return proxyList

    def GetProxyList(self):
        if SpiderProxy.proxyList==[]:
            return self.validateIp()
        else:
            return SpiderProxy.proxyList
