import turtle
from random import randint

#초기설정
김거북 = turtle.Turtle()
김거북.shape("circle")
각도 = [0, 90, 180, 270]
turtle.colormode(255)

#크기, 굵기, 속도, 이동거리 설정
창크기 = 400
거북크기 = 0.3
선굵기 = 10
이동 = 30
속도 = 10  # 1에서 10사이의 숫자 입력
반복횟수 = 200


#유저 입력을 바탕으로 설정
turtle.setup(width=창크기, height=창크기)
김거북.speed(속도)
김거북.shapesize(거북크기, 거북크기)
김거북.pensize(선굵기)


#색깔 설정
def color_change():
    색1 = randint(0, 255)
    색2 = randint(0, 255)
    색3 = randint(0, 255)
    김거북.color(색1, 색2, 색3)


#랜덤이동
def random_move():
    #방향설정
    방향 = 각도[randint(0,3)]
    김거북.right(방향)
    
    #색깔변경
    color_change()
    
    #이동
    김거북.forward(이동)


#범위 벗어나는 것 확인
def check_position():
    x축넘어감 = round(abs(김거북.xcor())) > (창크기 / 2)
    y축넘어감 = round(abs(김거북.ycor())) > (창크기 / 2)
    if x축넘어감 or y축넘어감:
        김거북.up()
        김거북.home()
        김거북.down()


#실제로 그리기
for i in range(반복횟수):
    check_position()
    random_move()



turtle.Screen()
turtle.Screen().exitonclick()