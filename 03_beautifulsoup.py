#訪問ptt頁面 籃球版
from urllib import request
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

req= request.Request(url =url, headers =headers)
res =request.urlopen(req)#把網址開起來，得到裡面的東西 (開啟request)
# print(res.read().decode('utf-8'))

#html字串轉beautiful型別
soup = BeautifulSoup(res.read(),'html.parser')
#soup不是字串，是 BeautifulSoup的物件型態
# print(soup)

#找批踢踢實業坊的logo
logo = soup.findAll #進行定位findall(標籤,屬性)
print(logo) #[<a href="/bbs/" id="logo">批踢踢實業坊</a>] 回傳一個list
print(logo[0]) #取list中的第0個，因為裡面只有一個東西
print(logo[0].text) #只取出內容，標籤以外都捨去
print(logo[0]['href']) #取得屬性herf的值 : 只取bbs字串 (網址只能自己拼湊)
print('http://www.ptt.cc'+logo[0]['href']) #拼湊網址
print(logo[0]['id'])

#屬性key當參數帶入
logo = soup.findAll('a', id='logo')
print(logo) #會跟上面屬性當字典的結果依樣

#select用法
logo_select = soup.select('a[id="logo"]')
print(logo_select )

#select選擇器方式
logos = soup.select('a#logo')
print(logos)