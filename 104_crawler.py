import requests
from bs4 import BeautifulSoup
import json
import os
import pandas as pd
import time

def job():
    ss = requests.session()
    #----------------------------------
    resource_path = (r'./104job')
    if not os.path.exists(resource_path):
         os.mkdir(resource_path)

    df = pd.DataFrame(columns=['招募日期', '公司名稱','職稱', '產業別', '地區', '工作內容', '薪資', '科系要求', '學歷要求',
                                       '招募網址', 'Python','MySQL', 'MongoDB','Linux', 'Django', 'TensorFlow', 'Docker'])
    #----------------------------------

    keyword = str(input("請輸入搜尋職缺:"))

    # isnew = int(input('請輸入__天內更新:'))
    # numbers = int(input('想蒐集__職缺?(建議一次30筆):'))

    #order看排序的(符合度排序、學歷排序) order =15(符合度)
    #asc為大到小或小到大) asc=0 最符合-最不符合 asc=1 最不符合到最符合

    all = []
    page = 1

    #----------------------------------

    for i in range(10):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

        url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%s&order=15&asc=0&page=%s&mode=s&jobsource=2018indexpoc'% (keyword, page)

        # url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python&order=15&asc=0&page=%s&mode=s&jobsource=2018indexpoc'%(page)
        res = ss.get(url=url, headers=headers)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')

        job_list = soup.select('article.job-list-item')

        # print(job_list)
        # print('##################################page###################################################################################', page)

    #------------------------------------------------
        for job in job_list:

            name = job.select('a')[0].text
            url = job.select('a')[0]['href'].split('/')[-1].split('?')[0]
            urla = 'https://www.104.com.tw/job/ajax/content/' + url
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
                , 'Referer': 'https://www.104.com.tw/job/' + urla}
            res = requests.get(url=urla, headers=headers)
            js = json.loads(res.text)
    #--------------------
            for each_element in js:
                # print(dict.keys(js))
                js_header = js['data']['header']
                js_jobDetail = js['data']['jobDetail']
                js_condition = js['data']['condition']
                industry = js['data']['industry']  # 4
                #公司基本資料    # print(dict.keys(js_header)) #dict_keys(['corpImageTop', 'jobName', 'appearDate', 'custName', 'custUrl', 'applyDate', 'analysisType', 'analysisUrl', 'isSaved', 'isApplied
                companyName = js_header['custName']#1
                jobName = js_header['jobName']#2
                appearDate = js_header['appearDate']#3
                #公司詳細資料#dict_keys(['jobDescription', 'jobCategory', 'salary', 'salaryMin', 'salaryMax', 'salaryType', 'jobType', 'workType', 'addressRegion', 'addressDetail', 'industryArea', 'longitude', 'latitude', 'manageResp', 'businessTrip', 'workPeriod', 'vacationPolicy', 'startWorkingDay', 'hireType', 'delegatedRecruit', 'needEmp'])
                addressRegion = js_jobDetail['addressRegion']#5
                Description = js_jobDetail['jobDescription']#6
                salary = js_jobDetail['salary']#7
                # #職務內容基本資料    # #dict_keys(['acceptRole', 'workExp', 'edu', 'major', 'language', 'localLanguage', 'specialty', 'skill', 'certificate', 'driverLicense', 'other'])'])
                edu = js_condition['edu']#9
                job_url = 'https://www.104.com.tw/job/' + url
                major = js_condition['major']  # 8
                if len(major) == 0:
                    major.append('不拘')

                # print(major)
                #---------------------------

                specialty = js_condition['specialty']  # 10
                specialty_value = list(set(val for dict in specialty for val in dict.values()))
                #----------------------------
                Python = 0
                MySQL = 0
                MongoDB = 0
                Linux = 0
                Django = 0
                TensorFlow = 0
                Docker = 0
                # ----------------------------
                if 'Python' in specialty_value:
                    Python += 1
                if 'MySQL' in specialty_value:
                    MySQL += 1
                if 'MongoDB' in specialty_value:
                    MongoDB += 1
                if 'Linux' in specialty_value:
                    Linux += 1
                if 'Django' in specialty_value:
                    Django += 1
                if 'TensorFlow' in specialty_value:
                    TensorFlow += 1
                if 'Docker' in specialty_value:
                    Docker += 1


                ej = []
                ej.append(appearDate)#1
                ej.append(companyName)#2
                ej.append(jobName)#3
                ej.append(industry)#4
                ej.append(addressRegion)#5
                ej.append(Description)#6
                ej.append(salary)#7
                ej.append(major)#8
                ej.append(edu)#9
                ej.append(job_url)#10
                ej.append(Python)#11
                ej.append(MySQL)#12
                ej.append(MongoDB)#13
                ej.append(Linux)#14
                ej.append(Django)#15
                ej.append(TensorFlow)#16
                ej.append(Docker)#17
                time.sleep(0.5)
            all.append(ej)

                    #print('已新增'+str(len(ej))+'筆資料')
            if len(all) != 0:
                print('已新增%s資料' % str(len(all)))
            else:
                print('file not found')

        print(all)
        #
        # except:
        #     break
        page += 1
    #
    a_df = df.append(pd.DataFrame(all, columns=['招募日期', '公司名稱', '職稱', '產業別', '地區', '工作內容', '薪資',
                                                '科系要求', '學歷要求','招募網址', 'Python', 'MySQL', 'MongoDB',
                                                'Linux', 'Django','TensorFlow', 'Docker']))
    a_df = a_df.drop_duplicates('招募網址')
    b_df = a_df.sort_values(by='招募日期', ascending=False)
    b_df.to_csv(r'./104job/%s.csv' % (keyword), index=False, encoding='utf-8-sig')

    return all
if __name__ == '__main__':
    result = job()