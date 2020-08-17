

c =""" 
vet: 10ahUKEwiiobqJ35frAhUEK6YKHSPmC-QQoEQIMygA..i
ei: Nvc0X6KuK4TWmAWjzK-gDg
rlz: 1C1SQJL_zh-TWTW836TW836
yv: 3
tbm: lcl
fll: 0,0
fspn: 9.037903116619788,3.504562564194174
fz: 0
sll: 0,0
sspn: 9.037903116619788,3.504562564194174
sz: 0
tbs: lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9
q: 台北 酒吧 地圖
start: 0
asearch: rl_ist
async: num:20,idx:0,hdr:true,stick:,_id:rl_ist0,_pms:s,_fmt:pc
"""


data1 = {}
for r in c.split('\n'):
    if r.strip() != '': #這樣其中有空值或空白都可以避免出錯，只取有值的地方
        data1[r.split(': ')[0]] = r.split(': ')[1]
print(data1)