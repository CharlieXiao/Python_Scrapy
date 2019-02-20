from bs4 import BeautifulSoup
import requests
import re
import time
import os

global pic,page,picurl,Url,ComicUrl_Pre

pic = re.compile(r'[-_/\w\d\.]{1,128}\.jpg')

page = re.compile(r'共(\d*)页')

ComicUrl_Pre = "http://n9.1whour.com/"

address = "http://comic.kukudm.com/comiclist/6/"

Url = "http://comic.kukudm.com"

Urls = []

Pics = []

def OpenUrl(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return False


def GetEpiUrl(url):
    print("获取章节信息...")
    Urls = {}
    html = OpenUrl(url)
    if html:
        soup = BeautifulSoup(html,"html.parser")
        # 每一章节的漫画保存在“comiclistn”的目录下
        for i in soup.find(id = "comiclistn").find_all('dd'):
            #获取每一章的链接
            add = Url + str(i.find('a').get('href'))
            #获取每一章的名字
            name = i.find('a').get_text()
            Urls[name] = add
    return Urls

def GetPicUrl(url):
    print("获取图片信息...")
    text = OpenUrl(url)
    PicList = []
    if text:
        #获取页码数
        p = int(page.search(text).group(1))
        for i in range(1, p+1):
            #u = picurl.search(url).group(0) + str(i) + ".htm"
            u = url.rpartition('/')[0] + '/' + str(i) + '.htm'
            text = OpenUrl(u)
            if text:
                PicList.append(ComicUrl_Pre + pic.search(text).group(0))
    return PicList


def DownloadPic(eps):
    #在D盘下新建bleach目录
    path = 'D:/Bleach'
    #判断路径是否存在
    if not os.path.exists(path):
        os.mkdir(path)
    #切换目录
    os.chdir(path)
    #遍历章节字典
    #for key,value in eps.items():
    kv = eps.popitem()
    sub_path = path + '/' + kv[0]
    os.mkdir(sub_path)
    os.chdir(sub_path)
    print('正在下载 ', kv[0], )
    i = 1
    pics = GetPicUrl(kv[1])
    if len(pics) == 0:
        print("图片信息获取失败")
        return
    else:
        for pic in pics:
            print('开始下载第', i, '张')
            p = requests.get(pic)
            pic_name = sub_path + '/' + str(i) + '.jpg'
            i = i + 1
            with open(pic_name, 'wb') as f:
                f.write(p.content)
            #os.chdir(path)

#time_start = time.time()
#l = GetPicUrl("http://comic.kukudm.com/comiclist/6/1748/1.htm")
#time_end = time.time()
#print("time_cost",time_end-time_start,"s")

start_time = time.time()
d = GetEpiUrl(address)
DownloadPic(d)
end_time = time.time()

print('下载结束，耗时 ', end_time-start_time, 's')

