from bs4 import BeautifulSoup
import lxml
import html5lib
import urllib
import bs4
import re
import requests

'''
Beautiful Soup类的基本元素
Tag             标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾
Name            标签的名字，<p>...</p>的名字是'p'，格式：<tag>.name
Attributes      标签的属性，字典形式组织，格式：<tag>.attrs
NavigableString 标签内非属性字符串,<>...</>中字符串，格式：<tag>.string
Comment         标签内字符串的注释部分，一种特殊的Comment类型

可以通过以下方法获取具体信息
.<tag>
.name
.attrs
.string
'''

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
# BeautifulSoup类代表一个html文档，html标签树
soup = BeautifulSoup(demo, "html.parser")


'''
html的基本遍历方式 上行遍历 平行遍历 下行遍历
下行遍历
.contents       子节点的列表，将<tag>所有儿子节点存入列表
.children       子节点的迭代类型，与.contents类似，用于循环遍历儿子节点
.descendants    子孙节点的迭代类型，包含所有孙子节点，用于循环遍历

上行遍历
.parent     节点的父亲标签
.parents    节点先辈标签的迭代类型，用于循环遍历先辈节点

平行遍历（必须发生在同一个父亲节点之下的各个节点间）
.next_sibling           返回按照HTML文本顺序的下一个平行节点标签
.previous_siblings      返回按照HTML文本顺序的上一个平行节点标签
.next_siblings          迭代类型，返回按照HTML文本顺序的后续所有平行节点标签
.previous_siblings      迭代类型，返回按照HTML文本顺序的前续所有平行节点标签
'''

'''
prettyfy()调试输出更加友好地输出HTML文件
'''

'''
信息的标记
信息标记的三种形式
XML     扩展标记语言 
JSON    JavaScript中面向对象信息的表达形式，有类型的键值对
YAML    无类型的键值对的信息的表达形式
'''

'''
信息提取的一般方式
方法一：完整解析信息的标记形式，再提取关键信息
方法二：无视标记形式，直接搜索关键信息
融合方法：结合形式解析与搜索方法，提取关键信息
'''
# print(type(soup.body.descendants)) # <class 'generator'> 迭代类型

#提取HTML中所有URL链接
'''
找到所有的<a>标签
解析<a>标签格式，提取href后的链接内容
'''
for link in soup.find_all('a'):
    print(link.get('href'))

'''
find_all(name,attrs,recursive,string,**kwargs)
返回列表类型，存储查找的结果
只填一个true代表查找所有标签
name:对标签名称的检索字符串(也可以是一个列表['a','b']就是查找所有a和b标签)
attrs:对标签属性值的检索字符串，可标注属性检索
recursive:是否对子孙全部检索，默认True
string:<>...</>中字符串区域的检索字符串

<tag>(..)等价于<tag>.find_all(..)
soup(..)等价于soup.find_all(..)
'''

