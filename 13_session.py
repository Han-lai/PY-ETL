import requests
from bs4 import BeautifulSoup


headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
url = 'https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html'
#這個頁面會帶到/ask/over18 自動去設定cookies(如果我們有正確取得post data

#建立共同session
ss = requests.session()   #所有的request都要放在這個session裡面
print(ss.cookies)  #<RequestsCookieJar[]> cookie裡面沒有任何東西
#Sesson1
# res =requests.get(url, headers=headers)
res = ss.get(url, headers=headers) #把 requests.get改成 ss.get
soup = BeautifulSoup(res.text, 'html.parser')
button = soup.select('button[class="btn-big"]')[0] #取第0個
print(button) #我已滿18  <button class="btn-big" name="yes" type="submit" value="yes">我同意，我已年滿十八歲<br/><small>進入</small></button>
#取得post_data
print(button['name']) #data-key值 yes
print(button['value'])#data-value值 yes


#找hidden data
hidden = soup.select('input')
print(hidden) #[<input name="from" type="hidden" value="/bbs/Gossiping/index.html"/>]


data = {}
data[button['name']] = button['value'] #取出其中key值跟value值 帶著這個post去訪問頁面
for k in hidden:
    data[k['name']] = k['value'] #hidden的key&value name="from" value="/bbs/Gossiping/index.html"/>]
print(data) #帶著yes yes 的結果訪問頁面 {'yes': 'yes', 'from': '/bbs/Gossiping/index.html'}


#Sesson2
target_url = 'https://www.ptt.cc/ask/over18' #要訪問的頁面
# res_target = requests.post(target_url, data=data, headers=headers)
res_target = ss.post(target_url, data=data, headers=headers)#requests.post改成ss.post

#Sesson3
final_url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
final_res = ss.get(final_url, headers=headers) #requests.get改成ss.get
print(final_res.text)


#session裡面的cookie長什麼樣子
print(ss.cookies) # <RequestsCookieJar[<Cookie __cf_bm=dd9f37be4f448fe2d2aa15ab080352d853b4951e-1590220198-1800-AUV8uy7I5WEQk/Q/bfEbwyys42nZ8b4Jx+oPwy2E4O+rCoH9HmzC96gvb1XRhwolmCFywYuvo1RUc+lyGD6lgi8=
# for .ptt.cc/>, <Cookie __cfduid=de6cdbbea2de11d6387cd377fb2745d641590220198 for .ptt.cc/>, <Cookie over18=1 for www.ptt.cc/>]>自動設成1
