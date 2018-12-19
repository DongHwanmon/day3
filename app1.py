import requests
import random

from bs4 import BeautifulSoup as bs
# as를 쓰면 BeautifulSoup를 bs로 사용가능

url = 'https://m.dhlottery.co.kr/common.do?method=main'
response = requests.get(url).text
#print(response)
soup = bs(response, 'html.parser')
document = soup.select('.prizeresult')[0]
numbers = document.select('span')
ns = []
for number in numbers:
  ns.append(int(number.text))
  
print(ns)

numbers = range(1,46)
lotto_num=random.sample(numbers,6)
lotto_num.sort()#오름차순

print(lotto_num)
lotto_real = ns
#지난주 로또 번호와 추출된 랜덤 로또 번호가
#한번씩 순회 하면서 몇개가 맞았는지 카운트하기
cnt = 0
'''
for a in range(0,6) : 
  for b in range(0,6) :
    if(lotto_num[a] == lotto_real[b]):
      cnt+=1
      #lotto_real[b] = 0
'''   
for num in ns:
  if num in lotto_num: # 배열에서 어떤 요소가 있는지 확인하는 방법
    cnt=cnt+1
      

      
cnt_2nd = 0
      
print("맞춘숫자의 개수는 : {} ". format(cnt))

if cnt == 1:
  print("꼴등입니다..")
elif cnt == 2:
  print("꼴등입니다..")
elif cnt == 3:
  print("6등 5000원에 당첨되셧어요~")
elif cnt == 4:
  print("5등에 당첨되셧어요~")
elif cnt == 5:
    for b in range(0,6) :
      if(lotto_num[b] == lotto_real[6]):
        cnt_2nd+=1
        #lotto_real[b] = 0
      if(cnt_2nd==1):
        print("2등에 당첨되셧어요~ 축하드립니다~")
      else : 
        print("3등에 당첨되셧어요~ 축하드립니다~")
elif cnt == 6:
      print("1등에 당첨되셧어요~!!!!!!!!!!!!")
else:
    print("꼴등입니다..")
      
    
