from urllib import request
#輸入網址
url = 'http://ea4b5b22.ngrok.io/hello_get?name=Allen'
#提出要求 用urllib的功能urlopen，取得回應
res = request.urlopen(url)
# print(res) #回應html的字串
# print(res.read())
bstr = res.read()
html =bstr.decode('utf-8') #把爬下來的內容轉成字串型別(.decode)
print(html)  #印出為純字串的html



