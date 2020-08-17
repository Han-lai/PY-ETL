import requests
import json
from urllib import  request



headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.dcard.tw/service/api/v2/forums/game/posts?limit=30&before=233743555'

res = requests.get(url, headers=headers)  #用get 因為看網址李開發人員那邊是以get去訪問的
# print(res.text)  #直接回傳json而不是html 所以不用用bs4套件，要用json套件去解

json_data = json.loads(res.text) #把字串轉乘list 或dic的型態，依據字串外的中括號或大括號決定
#list的話可以用for迴圈去取出裡面的物件。
#觀察每一個物件，發現結構相似
# print(json_data[0])
# print('--------------------')
# print(json_data[1])
# print('--------------------')
# print(json_data[2])
# print('--------------------')
#
# #用for迴圈會把字典裡的key取出來(觀察每一個list的key是否依樣)
# for k in json_data[1]:
#     print(k)  #發現都樣所以可以確定每一個list可能是一篇文章
#
一
#取得標題，每一個t都是一個字典
for t in json_data:
    title_name = t['title']
    print(title_name)
    #取得文章網址
    #https://www.dcard.tw/f/job/p/233769078  #23376908為id ，沒有用單引號或其他東西瓜住，所以會自動轉成int
    title_url ='https://www.dcard.tw/f/game/p/' + str(t['id']) #所以要把id先轉成str的型態
    print(title_url)
    #取得圖片網址
    image_url_list =[ img['url'] for img in t['mediaMeta']] #雙層迴圈
    print(image_url_list) #印出圖片網址，告訴其中有幾張圖面
    #下載每一張圖片
    for image_url in image_url_list:
        # request.urlretrieve(image_url, './dcard_image/' + image_url.split('/')[-1])
        #用斜線分割並取最後一個，因為用文章標題當貯存名稱的話會出現os error 之類的 所以建議直接用圖片原始網址斜線後的當名稱
        #但用urllib可能會被擋住，因為這個方法沒有用到headers，還要設定其他複雜的
        #urllib.error.HTTPError: HTTP Error 403: Forbidden
        #所以改用request 下載圖片，直接取得圖片的二進制檔(binary)(當成文字檔在下載
        res_img = requests.get (image_url, headers=headers)
        image_content = res_img.content
        # print(image_content)
        with open('./dcard_image/' + image_url.split('/')[-1], 'wb') as f:  #wb是指write binary
            f.write(image_content)
        #OSError     : [Errno 22] Invalid argument: './dcard_image/96ae778c-9ce0-4937-8121-0f158b0d8306?r=0.5625'
        #若出現oserror 可以觀察後面的網址是不是出現非法字元，
        # 然後判斷說這個網址是不是圖片的，如果不是圖片的就不用理他，如果是圖片再去改檔名

        # 如果不是圖片的就不用理他?????