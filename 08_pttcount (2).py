import requests
from bs4 import BeautifulSoup
import os
import re

resource_path = input('filename:')
if not os.path.exists(resource_path):
     os.mkdir(resource_path)

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' }
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ss = requests.session()
ss.cookies['over18'] = '1'

# page_NO =38986
page_numbers = int(input('numbers:'))

for i in range(0, page_numbers):
    # url = 'https://www.ptt.cc/bbs/Gossiping/index{}.html'
    # res = ss.get(url.format(page_NO), headers=headers)
    res = ss.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    title_list = soup.select('div.title')

    for title in title_list:
        try:
            title_name = title.select('a')[0].text
            illegal = ['\\', '/', ':', '*', '?', '"', "'", '<', '>', '|']
            for i in illegal:  # 換掉所有非法字元
             title_name = title_name.replace(i, '_')

            title_url = title.select('a')[0]['href']
            # print('https://www.ptt.cc' + title_url)
            #內容
            content_url = 'https://www.ptt.cc' + title_url
            content_res = ss.get(content_url, headers=headers)
            content_soup = BeautifulSoup(content_res.text, 'html.parser')
            content = content_soup.select('div#main-container')[0].text.split('--')[0]
#-------------------------------------
            push_up = 0
            push_down =0
            score =0
            author = ''
            title = ''
            datetime = ''
#推文 噓文標籤---------------------------
            push_tag = content_soup.select('div[class="push"] span') #hl push-tag
            # push_up_tag = content_soup.select('span[class="hl push-tag"]')
            for tag in push_tag:
                if "推" in tag.text:
                    push_up += 1
                if "噓" in tag.text:
                    push_down += 1
            score = push_up-push_down
            # print("推", push_up)
            # print("噓",push_down)
            # print(score)

            content_infoa = content_soup.select('div[class="article-metaline"] span')
            content_info = enumerate(content_infoa) #把class="article-metaline裡的內容轉成索引值
            # print(content_info)
            for n, info in content_info:
                if (n + 1) % 6 == 2:
                    author = info.text
                    # print(author)
                if (n + 1) % 6 == 4:
                    title = info.text
                if (n + 1) % 6 == 0:
                    datetime = info.text

            content += '\n----------split--------------\n'
            content +='推: %s \n' % (push_up)
            content +='噓: %s \n' % (push_down)
            content +='分數: %s \n' % (score)
            content +='作者: %s \n' % (author)
            content +='標題: %s \n' % (title)
            content +='時間: %s \n' % (datetime)
            print(content)
            print('----------------------------------------------------------------------')
            with open('./%s/%s.txt' % (resource_path, title_name), 'w', encoding= 'utf-8') as f:
                f.write(content)
            # print(content)
        except IndexError as err:
            print(title)
            print('IndexError:', err)
        # except OSError as err:
        #     print('===============================')
        #     print('OSError:', err)
        #     print(title)
        #     print('===============================')
        # except FileNotFoundError as ferr:
        #     print('===============================')
        #     print('FileNotFoundError:', ferr)
        #     print(title)
        #     print('===============================')
        # except AttributeError as aerr:
        #     print('===============================')
        #     print('AttributeError:', aerr)
        #     print(title)
        #     print('===============================')




    # page_NO -= 1
    # print(url.format(page_NO))

    page_url_soup = soup.select('a[class="btn wide"]')
    # print(page_url_soup) #共有三個[0、1、2]
    last_page_url = 'http://www.ptt.cc'+ page_url_soup[1]['href'] #要上一頁所以是第1個，取出內部的href
    # print(last_page_url)

    url = last_page_url
