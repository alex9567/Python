from bs4 import BeautifulSoup
from bs4 import element
import re
#html为解析的页面获得html信息,为方便讲解，自己定义了一个html文件

html = """
<html>
<head>
<title>Jack_Cui</title>
</head>
<body>
<p class="title" name="blog"><b>My Blog</b></p>
<li><!--注释--></li>
<a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
<a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
<div id="content" class="showtxt">
aaa
<br /><br />
bbb
<br /><br />
ccc
</div>
</body>
</html>
"""

#创建Beautiful Soup对象
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())

print("soup中的四大对象Tag如下：")
print(soup.title)
#<title>Jack_Cui</title>

print(soup.head)
#<head> <title>Jack_Cui</title></head>

print(soup.a)
#<a class="sister" href="http://blog.csdn.net/c406495762/article/details/58716886" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a>

print(soup.p)
#<p class="title" name="blog"><b>My Blog</b></p>

#对象类型
print(type(soup.title))
#<class 'bs4.element.Tag'>

#name对象
print(soup.name)
print(soup.title.name)
#[document]
#title

#attrs对象
print(soup.a.attrs)
#{'class': ['sister'], 'href': 'http://blog.csdn.net/c406495762/article/details/58716886', 'id': 'link1'}
print(soup.a['class'])
print(soup.a.get('class'))
#['sister']
#['sister']

print("soup中的四大对象NavigableString如下：")
print(soup.title.string)
#Jack_Cui

print("soup中的四大对象BeautifulSoup如下：")
print(type(soup.name))
print(soup.name)
print(soup.attrs)
#<class 'str'>
#[document]
#{}

print("soup中的四大对象Comment如下：")
print(soup.li)
print(soup.li.string)
print(type(soup.li.string))
#<li><!--注释--></li>
#注释
#<class 'bs4.element.Comment'>

if type(soup.li.string) == element.Comment:
     print(soup.li.string)

#tag的content属性
print(soup.body.contents)

#输入方式为列表
print(soup.body.contents[1])

#children遍历子节点
for child in soup.body.children:
     print(child)

#搜索文档树
print(soup.find_all('a'))

#传递正则表达式
for tag in soup.find_all(re.compile("^b")):
     print(tag.name)
#body
#b
#br
#br
#br

#传递列表
print(soup.find_all(['title','b']))
#[<title>Jack_Cui</title>, <b>My Blog</b>]

#传递true
for tag in soup.find_all(True):
     print(tag.name)

#通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag。
print(soup.find_all(attrs={"class":"title"}))
#[<p class="title" name="blog"><b>My Blog</b></p>]

#通过 text 参数可以搜搜文档中的字符串内容，与 name 参数的可选值一样, text 参数接受字符串 , 正则表达式 , 列表, True。
print(soup.find_all(text="Python3网络爬虫(三)：urllib.error异常"))
#['Python3网络爬虫(三)：urllib.error异常']

# find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果。
print(soup.find_all("a", limit=1))
#只有一个结果，本来有3个tag
print("ceshi:")
print(soup.find_all('a'))