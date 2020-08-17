import requests
from bs4 import BeautifulSoup
import  os #要把文章存進去資料夾李

if not os.path.exists('pttmovie'): #看資料夾在不再  不再才創資料夾
    os.mkdir('pttmovie')

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/bbs/movie/index.html'

for i in range(0,5):
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
        try:
            title = title_soup.select('a')[0].text #標題
            print(title)
            title_url ='https://www.ptt.cc/' + title_soup.select('a')[0]['href'] #網址
            print(title_url)
            #step3-4對文章進行request 表示點進文章----------------
            res_article = requests.get(title_url, headers=headers)
            soup_article = BeautifulSoup(res_article.text, 'html.parser')
            # 取出文章內容，用maincontent做出定位-------------div#main-content------#main-content----------------
            article_content_list = soup_article.select('#main-content')  # 這樣子定位法div#main-content與 #main-content 結果會是一樣的 因為id-maincontent是唯一的
            # print(article_content_list[0].text) #回傳整個內容
            # print(article_content_list[0].text.split('※ 發信站')[0])  # 用※分割內容與留言
            article_content = article_content_list[0].text.split('※ 發信站')[0]
            # 用每個標題當作文字檔的名稱------------------
            try:
                with open('./pttmovie/%s.txt' % (title), 'w', encoding= 'utf-8') as f :
                    f.write(article_content)
            except FileNotFoundError as e:  #檔案名稱出現斜線 可以try except 也可已在開啟檔案時直接把斜線換掉
                print(e)
                print(title)
                with open('./pttmovie/%s.txt' % (title.replace('/', '-')), 'w', encoding='utf-8') as f:
                    f.write(article_content)
        #非法字元再寫一次try except--------------
            # except OSError  as e:  #檔案名稱出現非法字元
            # except OSError as e:

                    # OSError: [Errno 22]
                    # Invalid
                    # argument: './pttmovie/[請益] BVS 為何超人感受不到馬莎?.txt'
# --------------------------------------------------------------
            # 最後的文章內容----------------------
            # print(article_content)
            print('=============================================')

        except IndexError as e:
            print(title_soup)

#取得上一頁的網址
    page_url_soup = soup.select('a[class="btn wide"]')
    print(page_url_soup) #共有三個[0、1、2]
    last_page_url = 'http://www.ptt.cc'+ page_url_soup[1]['href'] #要上一頁所以是第1個，取出內部的href
    print(last_page_url)

    url = last_page_url
