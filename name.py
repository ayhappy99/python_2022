import turtle
t = None
t = turtle.Turtle()
t.shape('turtle')
s = turtle.textinput("","이름을 입력하시오:")
t.write("안녕하세요? 터틀 인사드립니다.")
for i in range(0,4):
    t.left(90)
    t.forward(200)
    
