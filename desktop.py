import re
import requests
import threading

def download(url):
    img_name = url.split('/')[-1]
    filename = r'D:\\wallpaper\\download\\' + img_name
    f = open(filename, 'wb')
    f.write(requests.get(url).content)
    f.close()
    print(url + '  --OK!')

def search(url):
    # print(url)
    # url = 'http://simpledesktops.com/browse/'
    site = requests.get(url)
    site_content = site.text
    edge = re.findall(r'<div class="desktops column span-24 archive">(.*)</div>', site_content, re.S)[0]
    imgs = re.findall(r'img src="(.*?).295x184_q100.png', edge, re.S)

    for img in imgs:
        threading.Thread(target=download, args=(img,)).start()

    # browse = re.findall(r'browse/\d+/', site_content, re.S)[0]
    # print(browse)
    global page
    if page > 10:
        return 0
    page += 1
    url = 'http://simpledesktops.com/browse/' + str(page) + '/'
    search(url)


if __name__ == '__main__':
    page = 1
    search(r'http://simpledesktops.com/browse/')