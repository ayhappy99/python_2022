import turtle

t = turtle.Turtle()

t.shape('turtle')
s = turtle.textinput("","몇각형:")
n = int(s)

for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
