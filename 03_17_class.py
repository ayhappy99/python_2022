Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.


print("100")
100
print("%d"%100)
100
print("100"+"100")
100100
print("100 + 100")
100 + 100
print("%d" % (100+100))
200
print("%d / %d = %d" % (100,200,0.5))
100 / 200 = 0
첫번째는 100 두번째는 200 세번째는0.5 맵핑됨
SyntaxError: invalid syntax
왜 0 ?
SyntaxError: invalid syntax
소수점은 decimal 로 받아서 표시안됨
SyntaxError: invalid syntax
%d 는 decimal %x는 hexa=16진수 %o는oct=8진수
SyntaxError: invalid decimal literal

5
%f 소수점 %c 한글자 %s 글자열  s쓰면 모든문자받을수있어서 s쓰는게편함
SyntaxError: invalid syntax
print("%5d" % 123)
  123
%5d 다섯자리로
SyntaxError: invalid decimal literal
%05d 다섯자리인데 빈자리는 0으로
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
%f는 소수점아래여섯자리까지무조건출력 %7.1f는 일곱자리에서 소수점아래 한자리까지만 출력 %7.3f는 일곱자리에서 소수점아래 셋째자리까지 출력 소수점아래자리에 빈칸은 0으로출력
SyntaxError: invalid decimal literal
%10s 는 열자리에서 오른쪽정렬로 출력함
SyntaxError: invalid decimal literal
print("%d %5d %05d" % (123, 123,123))
123   123 00123
print("{0:d} {1:5d} {2:05d}".format(123,123,123))
123   123 00123
print("{1:d} {2:5d} {0:05d}".format(123,234,456))
234   456 00123

==== RESTART: /Users/parkseonga/Documents/code03-02.py ====

 줄 바꿈 
 연습
for 변수 in range (시작값,끝값+1,증가값) ==for (int i=0,i<3,i++)
SyntaxError: expected ':'
for i in range (0,3,1):
    print("%d" %i)

    
0
1
2
bin(11)
'0b1011'
hex(11)
'0xb'
hex(0b1011)
'0xb'
0b는 이진수라는뜻 0x는 16진수 0o는 8진수
SyntaxError: invalid binary literal
bin(0xb)
'0b1011'

==== RESTART: /Users/parkseonga/Documents/code03-02.py ====
입력 진수 결정 (16//10/8/2/):16
값 인력: FF
16진수 ==> 0xff
10진수 ==> 255
8진수 ==> 0o377
2진수 ==> 0b11111111
int("fe",16)
254
//dkdkdk
SyntaxError: invalid syntax
#dfdf#
int("ff", 16)
255
int("rf",16)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int("rf",16)
ValueError: invalid literal for int() with base 16: 'rf'
r값을 사용안해서 에러난거임 !
SyntaxError: invalid syntax

========== RESTART: /Users/parkseonga/Documents/code03-02.py =========
[메뉴]
+아메리카노:2원,000원 카페라떼:3,000원 카푸치노:3500원

========== RESTART: /Users/parkseonga/Documents/code03-02.py =========
[메뉴]
+아메리카노:2,000원 카페라떼:3,000원 카푸치노:3500원

========== RESTART: /Users/parkseonga/Documents/code03-02.py =========
[메뉴]
아메리카노:2,000원 카페라떼:3,000원 카푸치노:3500원

========== RESTART: /Users/parkseonga/Documents/code03-02.py =========
[메뉴]
아메리카노:2,000원 카페라떼:3,000원 카푸치노:3500원
%d*2000 아메리카노 판매 개수:
