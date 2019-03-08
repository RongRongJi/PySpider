import SongSpider.music_index
import SongSpider.songURL
import SongSpider.songDetail

if __name__ == '__main__':
    musicSpider = SongSpider.music_index.music_index()
    songs = musicSpider.getSongs()
    urls = SongSpider.songURL.MusicURL(songs[0])
    details = []
    for i in range(len(songs)):
        urls.setSongs(songs[i])
        songurl=urls.getURL()
        songdetail = SongSpider.songDetail.MusicDetail(songurl)
        details.append(songdetail.startSpider())