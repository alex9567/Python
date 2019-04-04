import chardet
#当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
print(chardet.detect(b'Hello, world!'))
#检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
#我们来试试检测GBK编码的中文：
data = '离离原上草，一岁一枯荣'.encode('gbk')
print(chardet.detect(data))
#检测的编码是GB2312，注意到GBK是GB2312的超集，两者是同一种编码，检测正确的概率是74%，language字段指出的语言是'Chinese'。
#对UTF-8编码进行检测：
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
#我们再试试对日文进行检测：
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
#chardet支持检测的编码列表请参考官方文档Supported encodings。