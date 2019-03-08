import Spider.spider as s


class music_index:

    def __init__(self):
        self.url = 'https://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset=0'
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }

    def getSongs(self):
        spider = s.SpiderTemplate(header=self.headers,url=self.url)
        soup = spider.spider()
        #获取包含歌单详情页网址的标签
        ids = soup.select('.dec a')
        #获取包含歌单索引页信息的标签
        lis = soup.select('#m-pl-container li')
        songs = []
        #for j in range(len(lis)):
        for j in range(0,4):
            # 获取歌单详情页地址
            url = ids[j]['href']
            # 获取歌单标题,替换英文分割符
            title = ids[j]['title'].replace(',', '，')
            # 获取歌单播放量
            play = lis[j].select('.nb')[0].get_text()
            # 获取歌单贡献者名字
            user = lis[j].select('p')[1].select('a')[0].get_text()
            # 输出歌单索引页信息
            #print(url, title, play, user)
            songs.append([url,title,play,user])
        return songs

