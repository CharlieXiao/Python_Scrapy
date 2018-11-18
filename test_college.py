import bs4
import requests
from bs4 import BeautifulSoup
import re

# 定向爬虫实例
# 2018年大学软件科学排名

#chr(12288)表示中文字符

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)  # 添加连接超时的阙值
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    # 每一个tr标签包含了当前大学的所有的数据信息
    # 先获得tbody标签的内容
    # 再对tbody的内容进行解析
    for tr in soup.find('tbody').children:
        # 需要过滤掉非标签类型的其他信息
        if isinstance(tr,bs4.element.Tag):
            # tr标签中包含大学信息的内容位于td标签中
            tds = tr('td')
            # 将所需要的大学的信息添加到ulist中
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])



def printUnivLisr(ulist,num):
    #格式化输出
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学习名称","省份",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
    print("Suc"+str(num))



def main():
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    uinfo = []
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivLisr(uinfo,50) # 只打印出50所大学的相关信息

main()