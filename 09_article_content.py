import requests
from bs4 import BeautifulSoup
import re
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
title_url= 'https://www.ptt.cc/bbs/movie/M.1590058721.A.C94.html'
#爬文章內容

res_article = requests.get(title_url,headers = headers)
soup_article = BeautifulSoup(res_article.text,'html.parser')
# print(soup_article)

#取出文章內容
article_content_list = soup_article.select('#main-content')  #這樣子定位法div#main-content與 #main-content 結果會是一樣的 因為id-maincontent是唯一的
# print(article_content_list[0].text) #回傳整個內容
# print(article_content_list[0].text.split('※ 發信站')[0]) #分割內容與留言
article_content= article_content_list[0].text.split('※ 發信站')[0]
# con = re.compile(r'\D')
# m = con.match(article_content)
# print(m.group())

print(re.split('\d',article_content))
# print(article_content.split(r'\d'))