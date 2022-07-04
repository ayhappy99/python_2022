from tkinter import *
import time
import random

WIDTH = 800
HEIGHT = 400

class Ball:				
    def __init__(self, canvas, color, size, x, y, xspeed, yspeed):	
        self.canvas = canvas		# 캔버스 객체
        self.color = color		
        self.size = size		
        self.x = x			
        self.y = y			
        self.xspeed = xspeed		
        self.yspeed = yspeed		
        self.id = canvas.create_oval(x, y, x+size, y+size, fill=color)

    def move(self):			# Ball을 이동시키는 함수
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        (x1, y1, x2, y2) = self.canvas.coords(self.id)	# 공의 현재 위치를 얻는다.
        (self.x, self.y) = (x1, y1)
        if x1 <= 0 or x2 >= WIDTH:  
            self.xspeed = - self.xspeed		# 속도의 부호를 반전시킨다. 
        if y1 <= 0 or y2 >= HEIGHT:
            self.yspeed = - self.yspeed		# 속도의 부호를 반전시킨다.

bullets = []

# 이벤트를 처리하는 함수
def fire(event):
    bullets.append(Ball(canvas, "red", 10, 150, 250, 10, 0))
    

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind("<Button-1>", fire)	# 마우스 버튼 클릭 이벤트에 함수를 연

# 우리 우주선과 외계 우주선을 생성
spaceship = Ball(canvas, "green", 100, 100, 200, 0, 0)
enemy = Ball(canvas, "red", 100, 500, 200, 0, 5)

# 리스트에 저장된 각각의 객체들을 이동 
while True:
    for bullet in bullets:
        bullet.move()
        # 포탄이 화면을 벗어나면 삭제
        if (bullet.x+bullet.size) >= WIDTH: 
            canvas.delete(bullet.id)
            bullets.remove(bullet)
    enemy.move()
    window.update()
    time.sleep(0.03)
