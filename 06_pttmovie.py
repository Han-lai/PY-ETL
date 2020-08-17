import requests
from bs4 import BeautifulSoup

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'

#html字串
res = requests.get(url, headers=headers)
# print(res.text)
#轉成beautiful型態
soup = BeautifulSoup(res.text, 'html.parser')
title_list = soup.select(('div.title'))
# print(title_list)
#只取每一個標題

for title_soup in title_list:
    # print(title_soup)
    # title = title_soup.select('a') #用a定位
    title = title_soup.select('a')[0].text
    print(title) #標題
    bbs = title_soup.select('a')[0]['href'] #網址
    print('http://www.ptt.cc'+bbs)
