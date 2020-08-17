from selenium.webdriver import Chrome
import requests

driver = Chrome('./chromedriver') # 副檔名不用打

url ='https://www.ptt.cc/bbs/index.html'

driver.get(url) #對網址提出請求，便會自動開啟一個瀏覽器到所到網址李
driver.find_element_by_class_name('board-name').click()
driver.find_element_by_class_name('btn-big').click()


cookie = driver.get_cookies()

# driver.close()
ss = requests.session()
for c in cookie:
    ss.cookies.set(c['name'], c['value'])
    print(c)

