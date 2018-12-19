from flask import Flask, render_template
import requests
import time
from bs4 import BeautifulSoup as bs


app = Flask(__name__)
@app.route('/index')
def index():
    print("Hi")
    print("nice to meet you")
    return """
    <h1>여기 너무 덥다</h1>
    <img src = "https://is5-ssl.mzstatic.com/image/thumb/Purple118/v4/f3/a5/8d/f3a58ded-cb11-9347-037b-f23c70897df8/AppIcon-1x_U007emarketing-85-220-0-6.png/246x0w.jpg">
    <h3<br>Hello world 죽겠다</h3>
    """
    
@app.route('/naverToon')
def naver_toon():


    
    #today = date.today()
    #today_day = today.weekday()
    #print(today_day)
    today = time.strftime("%a").lower()#오늘 날짜 요일
    print(today)
    #네이버 웹툰을 가져올수 있는 주소를 찾는다 파악한다 url변수에 저장하고
    #해당주소로 요청을 보내 정보를 가져온다.
    #받은 정보를 뷰티플스프bs를 이용해서 검색하기 좋게 만든다.
    #네이버웹툰페이지로가서 내가 원하는 정보가 어디에 있는지 파악한다
    #내가 원하는 정보는 웹툰을 볼 수 있는 링크
    #오늘자 업데이트 된 웹툰들의 각각 리스트 페이지 , 그리고 웹툰의 제목+해당웹툰의 썸네일까지
    #3번에서 저장한 정보를 이용해서 4번에서 파악한 정보의 위치를 찾는다.
    naver_url = 'https://comic.naver.com/webtoon/weekdayList.nhn?week='+today
    response = requests.get(naver_url).text
    #print(response)
    soup = bs(response, 'html.parser')
    #찾을떄는 클래스 또는 각각의이름으로 찾는다?
    #print(soup)
    '''toons = [{"title":?,
             "url":?,
             "img_url":?}
    ]'''
    li = soup.select('.img_list li')#클래스 별명일떄는 .을 붙여서 검색
                                     #ID로 검색할떄는 #아이디로 검색
                                     #빈칸을 띄우면 그 클래스 안에 있는것에서 li를 검색한다는 의미
    toons = []
    '''
    for item in li:
      toon = {"title":item.select('dt a')[0].text,#같은의미 "title":item.select_one('dt a').text
              "url":item.select('dt a')[0]["href"],
              "img_url":item.select('.thumb img')[0]["src"]#src라는 키값으로 값을 구한다는 의미
      }
      
      '''
      
    for item in li:
      toon = {"title":item.select('.thumb a')[0]["title"],#같은의미 "title":item.select_one('dt a').text
              "url":item.select('.thumb a')[0]["href"],
              "img_url":item.select('.thumb img')[0]["src"]#src라는 키값으로 값을 구한다는 의미
      }
      
      toons.append(toon)
    
    
    return render_template('naver_toon.html',t=toons) #별명이 없을떄는 그냥 쓰면된다
    
@app.route('/daumToon')
def daum_toon():
    
    return render_template('naver_toon.html')#이 파일은 틀이기때문에 가져다 써도 된다 (재활용해도 된다)
    