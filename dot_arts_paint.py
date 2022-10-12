from turtle import Turtle, Screen, colormode, setup
from random import randint

#기본세팅
거북 = Turtle()
거북.up()
colormode(255)


#도트 모양, 크기, 간격설정
거북.shape("circle")
    #가능한 모양 "arrow" "turtle" "circle" "square" "triangle" "classic"
가로크기 = 0.3
세로크기 = 0.3
외곽선 = 1
간격 = 20
창크기 = 300
속도 = "fastest"

#적용세팅
거북.speed(속도)
가로시작점 = -(창크기 / 2 - 간격) 
세로시작점 = -(창크기 / 2 - 간격) 
거북.shapesize(가로크기, 세로크기, 외곽선)
반복횟수 = round(창크기/간격 -1)

#숨기고 시작위치설정
거북.ht()
거북.setpos(가로시작점, 세로시작점)
setup(width=창크기, height=창크기)


def color_stamp():
    #색깔변경
    색깔1 = randint(0,255)
    색깔2 = randint(0,255)
    색깔3 = randint(0,255)
    거북.color((색깔1, 색깔2, 색깔3))

    #도장찍고 이동
    거북.stamp()
    거북.forward(간격)


#가로로 그리기 작업
def 가로그리기():
    for i in range(반복횟수):
        color_stamp()

#세로로 올리기 작업
def 세로이동():
    global 세로시작점
    세로시작점 += 간격
    거북.setpos(가로시작점, 세로시작점)

#그리기
for i in range(반복횟수):
    가로그리기()
    세로이동()


Screen()
Screen().exitonclick()