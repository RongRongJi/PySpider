import Spider.spider as s


class MusicURL:
    def __init__(self,songs):
        self.headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.songs= songs
        self.url = 'https://music.163.com'+songs[0]  #网址
        self.title = songs[1]   #标题
        self.play = songs[2]  #播放量
        self.user = songs[3]  #贡献者

    def setSongs(self,songs):
        self.songs= songs
        self.url = 'https://music.163.com'+songs[0]  #网址
        self.title = songs[1]   #标题
        self.play = songs[2]  #播放量
        self.user = songs[3]  #贡献者

    def getURL(self):
        spider = s.SpiderTemplate(header=self.headers, url=self.url)
        soup = spider.spider()
        # 获取歌单标题
        title = soup.select('h2')[0].get_text().replace(',', '，')
        # 获取标签
        tags = []
        tags_message = soup.select('.u-tag i')
        for p in tags_message:
            tags.append(p.get_text())
        # 对标签进行格式化
        if len(tags) > 1:
            tag = '-'.join(tags)
        else:
            tag = tags[0]
        # 获取歌单介绍
        if soup.select('#album-desc-more'):
            text = soup.select('#album-desc-more')[0].get_text().replace('\n', '').replace(',', '，')
        else:
            text = '无'
        # 获取歌单收藏量
        #collection = soup.select('#content-operation i')[1].get_text().replace('(', '').replace(')', '')
        # 歌单播放量
        #play = soup.select('.s-fc6')[0].get_text()
        # 歌单内歌曲数
        #songs = soup.select('#playlist-track-count')[0].get_text()
        # 歌单评论数
        #comments = soup.select('#cnt_comment_count')[0].get_text()
        # 输出歌单详情页信息
        #print(title, tag, text, collection, play, songs, comments)
        # 获得歌单标签
        tags=[] #标签集
        urls=[] #歌曲url
        u_tag = soup.select('.u-tag')
        for i in u_tag:
            tags.append(i.get_text())
        # 获取歌单内歌曲名称
        li = soup.select('.f-hide li a')
        for j in li:
            urls.append(j['href'])
        return [tags,urls]

