from urllib import request
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

req= request.Request(url =url, headers =headers)
res =request.urlopen(req)
# print(res.read().decode('utf-8'))

soup = BeautifulSoup(res.read(),'html.parser')

#定位標籤
# print(soup.select('a')) #定位a出現太雜的東西

#定位a標籤上一層的class="title"
title = soup.select('div.title') #得到的list每個東西都是beautifulsoup的東物件
# print(title) #獲得長得像標題的html

print('第0個',title[0])
print(title[0].select('a')) #也是brautiful的東西也可以進行select
print(title[0].select('a')[0])
print(title[0].select('a')[0].text) #只獲取內容
print('http://www.ptt.cc' + title[0].select('a')[0]['href']) #獲取網址

#進階 把下一層標籤變成其中一個變數
print(title[0].a.text)
print(title[0].a) #只會回傳第一個 (可查sibling)
