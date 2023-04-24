import requests
import time
import json
import time

session = requests.session()
def main2():
        headers={
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }


        params = {
        'username': '',
        'password': ''
        }
        url='https://manager.5idream.net/index.html'

        #访问jssm
        #访问数据接口
        res=session.post(url,headers=headers,params=params)
        cookie = res.cookies

        if res.status_code ==200:
                print("登陆成功",res.status_code)
        else:
                print("登陆失败",res.status_code)
        """
        :return: 获取精确毫秒时间戳,13位
        """
        return cookie
def main3(cookie=main2()):
        zeng2 = 1
        while zeng2 < 5:
                millis = int(round(time.time() * 1000))
                url2='https://manager.5idream.net/task/workorder/list?isDisplayExpire='+str(zeng2)+'&_search=false&nd='+str(millis)+'&rows=20&page=1&sidx=id&sord=desc&ordertype=&name=&refid=&catalogid1=&catalogid2=&className=&collegeId='
                zeng2 = zeng2+1
        else:
                print('这一页读取完咯')

        data2 = {
                'isDisplayExpire': '1',
                '_search': 'false',
                'nd': '1682318456697',
                'rows': '20',
                'page': '1',
                'sidx': 'id',
                'sord': 'desc',
                'ordertype': '',
                'name': '',
                'refid':'' ,
                'catalogid1': '',
                'catalogid2': '',
                'className': '',
                'collegeId': ''
                }
        res2 = requests.get(url=url2,data=data2,cookies=cookie).json()
        rows =res2['rows']
        rows2 = json.dumps(rows,ensure_ascii=False)
        rows3 = json.loads(rows2)
        zeng = 0
        while zeng < 20:
                print(rows3[zeng]['name']+rows3[zeng]['sendusername']+rows3[zeng]['collegename'])
                zeng = zeng+1
        else:
                print('这一页读取完咯')


zeng3 =0
while zeng3 < 20:
        main2()
        main3()
        zeng3=zeng3+1
else:
        print('完事咯')



