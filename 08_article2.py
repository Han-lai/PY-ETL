import requests
from bs4 import BeautifulSoup

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0,1):
    #html字串
    res = requests.get(url, headers=headers) #對url進行request 得到response ==一個html的字串
# print(res.text)
#轉成beautiful型態
    soup = BeautifulSoup(res.text, 'html.parser') #把html轉成beautifulsoup的型態
    title_list = soup.select(('div.title'))
# print(title_list)
#只取每一個標題
    #
    for title_soup in title_list: #把每一個soup都取出來
        print(title_soup)
        title = title_soup.select('a') #用a定位
        try:
            title = title_soup.select('a')[0].text  #在對soup進行select，用tect取出內容
            print(title) #標題
            bbs ='https://www.ptt.cc/' + title_soup.select('a')[0]['href'] #取出網址
            print(bbs)
        except IndexError as e:
            print(title_soup)

    # #取得上一頁的網址
    page_url_soup = soup.select('a[class="btn wide"]')
    print(page_url_soup) #共有三個[0、1、2]
    last_page_url = 'http://www.ptt.cc'+ page_url_soup[1]['href'] #要上一頁所以是第1個，取出內部的href
    print(last_page_url)

    url = last_page_url
