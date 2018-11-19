'''
候选数据网站的选择
选取原则：股票信息静态存储于HTML页面中，非js代码生成，没有Robots协议限制
选取方法：浏览器F12,源代码查看等

需要的网址
查询股票代码
http://quote.eastmoney.com/stocklist.html
所需的个股信息
https://gupiao.baidu.com/stock/+(所在的地区深圳为sz，上海为sh)+股票代码.html

先获取股票代码然后再再百度股票中查找股票的信息
'''

import requests
from bs4 import BeautifulSoup
import traceback
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst,stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html,'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url = stockURL+stock+".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html,'html.parser')
            stockInfo = soup.find('div',attrs={'class':'stock-bets'})

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称':name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
            with open(fpath,'a',encoding= 'utf-8') as f:
                f.write(str(infoDict)+'\n')
        except:
            traceback.print_exc()
            continue
    return ""

def getInfo(url):
    html = getHTMLText(url)
    try:
        if html == "":
            return {}
        infoDict = {}

        soup = BeautifulSoup(html,'html.parser')
        stockInfo = soup.find('div',attrs={'class':'stock-bets'})
        print(stockInfo)
        name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
        print("\n")
        print(name.text)
        infoDict.update({'股票名称': name.text.split()[0]})

        keyList = stockInfo.find_all('dt')
        valueList = stockInfo.find_all('dd')
        for i in range(len(keyList)):
            key = keyList[i].text
            val = valueList[i].text
            infoDict[key] = val
        print(str(infoDict))
        return infoDict
    except:
        traceback.print_exc()
        return {}

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = 'D://BaiduStockInfo.txt'
    slist = []
    getStockList(slist,stock_list_url)
    #getStockInfo(slist,stock_info_url,output_file)
    url = stock_info_url + slist[0] + ".html"
    print(url)
    sdict = getInfo(url)


main()
