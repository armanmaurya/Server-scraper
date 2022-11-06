import urllib.request

class DownloadVideo(object):

    def videoLink(url):


        url_link = url

        urllib.request.urlretrieve(url_link, 'video_name.mp4')


