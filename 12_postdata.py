import requests
url = 'http://ea4b5b22.ngrok.io/hello_post'
res_get = requests.get(url)
print(res_get.text) #不會出現<h1>Hello HAN !!</h1>
print('-----------------------')

#製作post data $有表單的網頁幾乎都這樣子代post data


data = {'username':'HAN'}
res_post = requests.post(url, data=data)
print(res_post.text)  #下面就會出現<h1>Hello HAN !!</h1>


