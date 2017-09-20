# -*- coding:UTF-8 -*-	
from bs4 import BeautifulSoup
from bs4 import element
import re
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
#创建Beautiful Soup对象
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title)
print(soup.head)
print(soup.a)
print(soup.p)
print(type(soup.a))
print(soup.head.name)
print(soup.p.attrs)
print(soup.p['class'])
print(soup.p.get('class'))
#soup.p['class']='newClass'
#del soup.p['class']
print(soup.p)
print(soup.p.string)
print(type(soup.name))
print(soup.name)
print(soup.attrs)#空字典
print(soup.a)
print(soup.a.string)
print(type(soup.a.string))
if type(soup.a.string)==element.Comment:
	print(soup.a.string)
print(soup.head.contents)
print(soup.head.contents[0])
print(soup.head.children)
for child in soup.head.children:
	print(child)
for child in soup.descendants:
	print(child)
print(soup.title.string)
print(soup.head.string)
for string in soup.strings:
	print(repr(string))
p = soup.p
print(p.parent.name)
print(soup.p.parent.name)
content = soup.head.title.string
print(content.parent.name)
for parent in content.parents:
	print(parent.name)
print(soup.p.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)
for sibling in soup.a.next_sibling:
	print(repr(sibling))
print(soup.head.next_element)
print(soup.find_all('b'))
print(soup.find_all('a'))
for tag in soup.find_all(re.compile('^b')):
	print(tag.name)
print(soup.find_all(['a','b']))
for tag in soup.find_all(True):
	print(tag.name)
def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')
print(soup.find_all(has_class_but_no_id))
print(soup.find_all(id='link2'))
print(soup.find_all(href=re.compile("elsie")))
print(soup.find_all(href=re.compile("elsie"),id='link1'))
print(soup.find_all('a',class_='sister'))
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={'data-foo':'value'})
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=["Tillie"]))
print(soup.find_all(text=re.compile('Dormouse')))
print(soup.find_all('a',limit=2))
print(soup.html.find_all('title'))
print(soup.html.find_all("title",reversed=False))
print(soup.select('title'))
print(soup.select("a"))
print(soup.select("b"))
print(soup.select('.sister'))
print(soup.select("#link1"))
print(soup.select('p #link1'))
print(soup.select('head > title'))
print(soup.select('a[class="sister"]'))
print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('p a[href="http://example.com/elsie"]'))
print(type(soup.select('title')))
print(soup.select('title')[0].get_text())

for title in soup.select('title'):
	print(title.get_text)
