import requests
from bs4 import BeautifulSoup
#爬取多頁的資訊
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

#先給url的最後一個format{}
url = 'https://www.ptt.cc/bbs/movie/index{}.html'

page = 8974 #到網頁上看首頁網址的頁碼是什麼數字
for i in range(0,5): #只爬五頁
    res = requests.get(url.format(page), headers=headers) #html字串 #url.format(page)
    soup = BeautifulSoup(res.text, 'html.parser')#轉成beautiful型態
    title_list = soup.select(('div.title'))
    # print(title_list)#只取每一個標題
    for title_soup in title_list:
        # print(title_soup)
        # title = title_soup.select('a') #用a定位
        try :
            title = title_soup.select('a')[0].text
            print(title) #標題
            bbs = title_soup.select('a')[0]['href'] #網址
            print('http://www.ptt.cc'+bbs)
        except IndexError as e:
            print(e)
            print(title_soup)
    page-= 1 #一直翻頁的