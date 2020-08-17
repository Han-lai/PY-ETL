from selenium.webdriver import Chrome
import time

driver = Chrome('./chromedriver') # 副檔名不用打

url ='https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dzh-TW%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&hl=zh-TW&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
driver.get(url)

time.sleep(5) #防止網頁跑太快可以先休息五秒再繼續跑
driver.find_element_by_id('identifierId').send_keys('sh1995lai@gmail.com') #輸入信箱的標籤
driver.find_element_by_id('identifierNext').click() #按繼續的地方
