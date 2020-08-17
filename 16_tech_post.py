import requests
import json
from bs4 import BeautifulSoup


url = 'https://buzzorange.com/techorange/wp-admin/admin-ajax.php'
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

#post提出的要求 要用data 在network裡看form  data 有什麼
data = {'action': 'fm_ajax_load_more',
        'nonce': 'd8c08f1381',
        'page': '1'}

res = requests.post(url, headers=headers, data=data)
json_data = json.loads(res.text)
# print(json_data) #最外層是大括號，所以氏字典
# print(json_data.keys()) #看裡面什麼key值
# print(json_data['data']) #出現兩個key data 跟susccess ，data 看起來是html，觀察裡面的真的是向html，所以要用bs4去解


soup = BeautifulSoup(json_data['data'],'html.parser')
title_list = soup.select('a[class="post-thumbnail nljf"]')
# print(title_list)
# <a class ="post-thumbnail nljf" href="https://buzzorange.com/techorange/2020/05/29/gogoro-ebike-giant/" aria-hidden="true"
# onclick="ga('send', 'event', 'TO Home Posts', 'Click', '【比機車還貴？】Gogoro 自推「智慧單車」要價 11.7 萬，其實捷安特更貴',
# {'nonInteraction': 1});" data-src="https://buzzorange.com/techorange/wp-content/uploads/sites/2/2020/05/gogoro-bike.webp?jpg" >
# & nbsp; < / a >
for t in title_list:
    # print(t)
    print(t['onclick'].split(',')[-2]) #取onclick 等號後的值，並觀察發現標題在倒數第二個，所以可以用逗點分割並取倒數第二個