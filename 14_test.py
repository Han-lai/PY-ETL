import requests
from bs4 import BeautifulSoup

url = 'http://e5918cb4.ngrok.io/practice/100'

headers = {'user-agent': '123'}

ss = requests.session()

res = ss.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
key = soup.select('input')[1]['name']
value = soup.select('input')[1]['value']
print(key, value)

data = {key: value, 'pwd': 'name123'} #看輸入名字之後出現的f12  form data那邊 需要兩個值  用字典的方式帶入
res = ss.post(url, data=data, headers=headers)
print(res.text)