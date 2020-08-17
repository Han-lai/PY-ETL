#訪問ptt頁面 籃球版
from urllib import request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Baseball/index.html'

req= request.Request(url =url, headers =headers)
res =request.urlopen(req)#把網址開起來，得到裡面的東西 (開啟request)

print(res.read().decode('utf-8'))
