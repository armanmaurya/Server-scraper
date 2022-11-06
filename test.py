from bs4 import BeautifulSoup
import requests
from downloadvideo import DownloadVideo
from fileDownloader import fileDownload



main_url = input("Enter the root directory Url : ")



def func(url):

    main_url = 'https://filepursuit.com/'

    html_page = requests.get(url).text
    soup = BeautifulSoup(html_page, 'lxml')
    meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
    
    for data in meta:
        link = data.find('a').get('href')
        rest_url = link
        urls = main_url + rest_url

        print('first page links: ' + urls)

        html_page = requests.get(urls).text
        soup = BeautifulSoup(html_page, 'lxml')
        meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
        for data in meta:
            link = data.find('a').get('href')
            rest_url = link
            urls = main_url + rest_url

            print('second page links:' + urls)

            html_page = requests.get(urls).text
            soup = BeautifulSoup(html_page, 'lxml')
            meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
            for data in meta:
                link = data.find('a').get('href')
                rest_url = link
                urls = main_url + rest_url

                print('third page links:' + urls)
                html_page = requests.get(urls).text
                soup = BeautifulSoup(html_page, 'lxml')
                meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
                for data in meta:
                    link = data.find('a').get('href')
                    rest_url = link
                    urls = main_url + rest_url

                    print('fourth page links:' + urls)
                    html_page = requests.get(urls).text
                    soup = BeautifulSoup(html_page, 'lxml')
                    meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
                    for data in meta:
                        link = data.find('a').get('href')
                        rest_url = link
                        urls = main_url + rest_url

                        print('fifth page links:' + urls)
                        html_page = requests.get(urls).text
                        soup = BeautifulSoup(html_page, 'lxml')
                        if soup.find('code'):
                            last_page = soup.find('code').text
                            print("Video links is : "+ last_page)

                        meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
                        for data in meta:
                            link = data.find('a').get('href')
                            rest_url = link
                            urls = main_url + rest_url
                            print('six page links:' + urls)


                            html_page = requests.get(urls).text
                            soup = BeautifulSoup(html_page, 'lxml')
                            if soup.find('code'):
                                last_page_link = soup.find('code').text
                                print("Video links is : "+ last_page_link)

                                vid = fileDownload.videoLink(last_page_link)
                                if vid:
                                        print('Your video is downloading')

                            meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
                            for data in meta:
                                link = data.find('a').get('href')
                                rest_url = link
                                urls = main_url + rest_url
                                print('seven page links:' + urls)

                                
                                html_page = requests.get(urls).text
                                soup = BeautifulSoup(html_page, 'lxml')
                                if soup.find('code'):
                                    last_page_link = soup.find('code').text
                                    print("Video links is : "+ last_page_link)
                                    vid = fileDownload.videoLink(last_page_link)
                                    if vid:
                                        print('Your video is downloading')



                                meta = soup.find_all('div', class_ = 'mb-4 mb-md-0 mr-6')
                                for data in meta:
                                    link = data.find('a').get('href')
                                    rest_url = link
                                    urls = main_url + rest_url

                                    print('eight page links:' + urls)
        


        
        


fist_link = func(main_url)














    






