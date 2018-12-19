"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q1=====")
summ=0
cnt=0
for i in iu_score:
    summ+=iu_score[i]
    cnt+=1
    
print(summ/cnt)
#1. iu_score라고 하는 dic변수에서 
#python get value
'''
scores = 0
scores = list(iu_score.values())
#python get values of dict
print(sum(scores)/len(scores))
#python get sum of list
#python get length of list
'''


# 2. 반 평균을 구하세요.
scores = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
'''
sum=0
cnt=0
for i in score:
    for a in score[i]:
        sum+=score[i][a]
        cnt+=1
print(sum/cnt)
'''
#각 반을 순회하는 반복문을 작성한다.
for cl in scores:
    #print(scores[cl])
#한 번 순회를 할 때 1번에서 작성한 코드를 활용한다.
    tmp = list(scores[cl].values())

#출력한다
#    print("{}".format(sum(tmp)/len(tmp)))

    print("{} : {}".format(cl, sum(tmp)/len(tmp)))

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}
#print(city)
#print(city.keys())

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")
'''
for i in city:
    summ = 0
    cnt = 0
    for a in range(3):
        #print(city[i][a])
        summ+=city[i][a]
        cnt+=1
        
    summ=summ/cnt
    print(city+sum)
'''

#tmp = list(scores[cl].values())
#문제3
#각 도시를 순회하는 반복문을 작성한다.
for city in cities:
    temp = cities[city]
    print(temp)
#위의 코드를 활용하여 순회할 때마다 평균 값을 출력한다.
    print("{}의 평균 기온 : {}" .format(city,round(sum(temp)/len(temp),1)))
    print("{}의 평균 기온 : {:5.1f}" .format(city,sum(temp)/len(temp)))
    



'''
coldest_place_x = ""
coldest_place_y = 0
hottest_place_x = ""
hottest_place_y = 0

for i in city:
    for a in range(2):
        if city[i][a]<city[i][a+1]:
            hottest_place_x = city[i]
            hottest_place_y = city[i][a+1]


        elif city[i][a]>city[i][a+1]:
            coldest_place_x = city[i]
            coldest_place_y = city[i][a]
   '''   

#print("가장 추운 도시: {} 온도 :{}".format(coldest_place_x,coldest_place_y))
#print("가장 더운 도시: {}".format(city[hottest_place_x]))





# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")

#문제3-1
#2.최저기온, 최고기온을 저장할 수 있는 변수를 선언한다.
minimum = ["도시명",1000]
maximum = ["도시명",-1000]
#1.각 도시를 순회하는 반복문을 만든다.
for city in cities:
    for temp in cities[city]:
        if minimum[1]>temp:
            minimum[0] = city
            minimum[1] = temp
        if maximum[1]<temp:
            maximum[0] = city
            maximum[1] = temp

print("최고 기온은 {}의 {}도 이며, 최저 기온은 {}의 {}도 입니다.".format(maximum[0],maximum[1],minimum[0],minimum[1]))

#3.각 도시의 기온 정보를 순회하는 반복문을 만든다.
#4.순회하다가 최저기온의 경우에는 현재 저장된 값보다 작은 갑이,
#  최고기온의 경우에는 현재 저장된 값보다 큰 값이 있는 경우
#  현재 저장되어 있는 값을 바꾼다.


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")

#1.cities 변수에서 서울부분만 추출한다.
#1-1. flag 라고 하는 변수에 false를 저장한다.
#2-1 서울 변수에서 서울부분만 추출해서 서울변수에 저장한다.
#2.2 서울 변수를 순회하며 요소가 2와 같았던 적이 있는지 확인한다.
#3. 2도와 같았던 적이 있다면 flag 변수를 true로 바꿔준다.
#4. flag 변수에 따라 출력문을 작성한다.

flag = false

for city in cities:
    if cities[city]=="서울":
        for temp in cities[city]:
            if temp == 2:
                flag = true
   
    '''
    if temp == 2:
       reply = "Yes" 

print(".".format(maximum[0],maximum[1],minimum[0],minimum[1]))
'''