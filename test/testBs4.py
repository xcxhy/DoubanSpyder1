'''
BeautifulSoup4将HTML文档转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种

-Tag
-NavigableString
-BeautifulSoup
-Comment
'''

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")
#print(bs.title)
#print(bs.a)
#print(bs.head)
#print(type(bs.head))
#1.tag  标签及其内容，显示标签的第一个内容

#print(type(bs.title.string))
#2.NavigableString 标签里的内容字符串

#print(bs.a.attrs)

#print(type(bs))

#3.BeautifulSoup  表示整个文档


#print(bs)

#4.注释
#print(bs.a.string)
#print(type(bs.a.string))


#---------------------------------------------

#文档的遍历
#print(bs.head.contents)
#print(bs.head.contents[1])

#更多内容搜索文档


#文档的搜索

#find_all()
#字符串过滤：会查找与字符串完全匹配的内容
#t_list = bs.find_all("a")
#print(t_list)

#正则表达式搜索：使用search()方法来匹配搜索
#import re
#t_list = bs.find_all(re.compile("a"))

#print(t_list)

#方法：传入一个函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)

#print(t_list)

#2.kwargs   参数

#t_list = bs.find_all(id = "head")
#t_list = bs.find_all(class_= True)
#t_list = bs.find_all(href = "http://news.www.baidu.com")


#3.text 参数
# t_list = bs.find_all(text =["地图","贴吧"] )
#
#
# t_list = bs.find_all("a",limit=3)
# for item in t_list:
#     print(item)


#4 css选择器

#t_list = bs.select('title')#  通过标签来查找
#t_list = bs.select(".mnav")  #通过类名来查找
#t_list = bs.select("#u1")   #通过id来查找
#t_list = bs.select("a[class= 'bri']")#通过属性来查找
#t_list = bs.select("head>title")  #通过子标签查找
# t_list = bs.select(".mnav~.bri")
#
# print(t_list[0].get_text())
# for item in t_list:
#     print(item)

