import random # 랜덤으로 숫자 받아오기

numbers = []  #리스트 변수에 아무것도 없는상태
for num in range (0,10) : # for문으로 10개의 숫자  0~9  
    numbers.append(random.randrange(0,10))  #append,random 으로 랜덤한 10숫자 추가

print("생성된리스트", numbers)

for num in range(0,10) :
    if num not in numbers :
        print("숫자 %d는 리스트에 없음" %num)
