import turtle
from random import randint

#초기설정
북 = turtle.Turtle()
북.speed("fastest")
turtle.colormode(255)

#색깔 설정
def color_change():
    색1 = randint(0, 255)
    색2 = randint(0, 255)
    색3 = randint(0, 255)
    북.color(색1, 색2, 색3)

#원의 반지름, 각도, 굵기설정
컬러1 = 북.color("gray")
반지름 = 100
각도 = 4
굵기 = 0.2

#사용자 설정에 따른 세팅
반복횟수 = round(360 / 각도)
북.pensize(굵기)

for i in range(반복횟수):
    color_change()
    북.circle(반지름)
    북.left(각도)

turtle.Screen()
turtle.Screen().exitonclick()
