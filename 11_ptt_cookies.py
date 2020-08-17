import requests
from bs4 import BeautifulSoup


headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {'over18':'1'} #在網頁上開cookie 看

res = requests.get(url, headers=headers, cookies=cookies)
print(res.text)   #<div class="over18-notice">

