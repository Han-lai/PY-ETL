import requests  #用requests 套件
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

#get的用法
res = requests.get(url,headers = headers)
print(res) #回傳200 訪問成功 5開頭伺服器問題 3警告 4網頁不見ex404
print(res.text) #秀出html的字串

#利用soup轉換

soup =BeautifulSoup(res.text,'html.parser')
print(soup)
