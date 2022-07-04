"""i, hap = 0 , 0

for i in range(0,100,7) :
    hap = hap + i

print("0과 100 사이에 있는 7의배수 합: %d" % hap)"""




"""i, hap = 0 , 0
num = 0

num = int(input(" 값을 입력하세요:"))

for i in range(1, num+1, 1) :
    hap = hap + i


print("1에서 %d 까지의 합계: %d" %(num,hap))"""





"""i, hap = 0 , 0
num1, num2, num3 = 0,0,0

num1 = int(input("시작값을 입력하세요:"))
num2 = int(input("끝값을 입력하세요:"))
num3 = int(input("증가값을 입력하세요:"))

for i in range(num1,num2 + 1, num3) :
    hap = hap + i

print("%d에서 %d까지 %d씩 증가시킨 값의 합계: %d" %( num1, num2, num3, hap))"""





"""i , dan = 0 ,0
dan  = int (input("단을 입력하세요:"))
for i in range(1,10,1):
    print("%d X %d = %2d" %  (dan,i,dan *i))"""





"""i,k = 0 , 0      ## 각 단의 제목이 출력되는 구구단##  
for i in range(2, 10, 1) :
    print("## %d단 ##" % (i))
    for k in range(1, 10, 1) :
        print("%d X %d = %2d" % (i, k, i*k))
    print("")"""





"""##전역변수선언부분##

i , k , guguLine = 0 , 0 , ""

for i in range(2,10) :
    guguLine = guguLine + (" #    %d단  # "  % i)    ## 단 제목 출력##

print(guguLine)

for i in range(1,10) :
    guguLine = ""
    for k in range(2,10) :
        guguLine = guguLine + str("%2d X %d = %2d  " % (k, i, k*i))

    print(guguLine)"""







"""hap = 0
a, b = 0, 0
while True :
    a = int(input("더할 첫 번째 수를 입력하세요:"))
    if a == 0 :
        break
    b = int(input("더할 두번째 수를 입력하세요:"))
    hap = a+b
    print("%d + %d = %d" % (a,b,hap))

print("0을 입력해 반복문을 탈출")"""







"""import turtle

t = turtle.Turtle()

t.shape('turtle')
s = turtle.textinput("","몇각형:")
n = int(s)

for i in range(n):      
    t.forward(100)
    t.right(360 / n)    """




i, k = 0,0

i= 0
while i < 9 :
    if i < 5 :
        k = 0
        while k< 4 -i :
            print(' ', end = '')
            k +=1

        k = 0
        while k <i * 2 +1:
            print('\u2605' , end = '')
            k += 1
    else :
        k = 0
        while k <i -4 :
            print(' ', end = '')
            k+=1
        k = 0
        while k < (9-i) *2-1 :
            print('\u2605', end = '')
            k+=1
    print()
    i+=1












