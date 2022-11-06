from tqdm import tqdm
import requests

class fileDownload(object):
    def videoLink(urls):

        chunk_size = 8192

        url = urls

        r = requests.get(url, stream = True)

        total_size = int(r.headers['content-length'])
        filename = url.split('/')[-1]

        with open(filename, 'wb') as f:
            print('Your download is starting')
            for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
                f.write(data)


        print("Download complete!")