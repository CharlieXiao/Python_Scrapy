import requests
import os
# import beautifulsoup4 as bs4

'''
Request对象的属性
r.status_code       HTTP访问请求，200代表访问成功，其他的代表访问失败
r.encoding          可能的编码方式
r.apparent_encoding 内容中可能的编码方式
r.text              网页的内容的字符串形式
r.content           网页内容的二进制形式
'''

'''
r = requests.get('http://www.baidu.com')

print(r.status_code)

print(r.encoding)

# 替换读取内容的编码方式
r.encoding = r.apparent_encoding

print(r.apparent_encoding)

print(r.text)

print(r.headers)
'''
'''
HTTP协议
URL格式 http://host[:port][path]
host:合法的Internet主机域名或IP地址
port:端口号，默认端口为80
path:请求资源的路径
URL是通过HTTP协议存储资源的Internet路径，一个URL对应一个数据资源
六个基本方法
GET HEAD POST PATCH PUT DELETE

request方法的可选访问参数
params  cookies proxies         cert
data    auth    allow_redirects
json    files   stream
headers timeout verify
'''

# 爬取网页的通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # 如果状态不是200，则引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

'''
if __name__ == "__main__":
    Url = "https://www.amazon.cn"
    try:
        r = requests.get(Url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        print("爬取失败")
        kv = {'user_agent': 'Mozilla/5.0'}
        r = requests.get(Url, headers=kv)
        print(r.status_code)
        r.encoding = r.apparent_encoding
        print(r.text)
        print(r.headers)
'''


'''
百度的关键词接口
http://www.baidu.com.s?wd=keyword

360的关键词接口
http://www.so.com/s?q=keyword

替换keyword就可以实现搜索
手动构造url链接

kv = {'q': 'Python'}
r = requests.get("http://www.so.com/s", params=kv)
print(r.status_code)
print(r.url)
'''
'''
网络图片的爬取和存储

网络图片链接的格式
http://www.example.com/picture.jpg
以.jpg结尾的为一个图片链接
'''

'''
# 图片爬取的代码



url = 'http://img0.dili360.com/ga/M02/49/B7/wKgBzFqo8ySAT4nUAAry7yQ0MW4188.tub.jpg@!rw17'
root = "D://pics//"
path = root + url.split('/')[-1].split('@')[0]


try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")
'''

'''
查询ip地址
http://m.ip138.com/ip.asp?ip=ipaddress
'''

url = "http://m.ip138.com/ip.asp?ip="
r = requests.get(url+'55.55.55.55')
print(r.text[-500:])


