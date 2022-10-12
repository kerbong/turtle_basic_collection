from turtle import Turtle, Screen
import turtle
from random import randint

색깔모음 = ["red", "orange", "yellow", "green", "blue", "purple", "indigo", "black"]
거북모음 = [1,2,3,4,5,6,7,8]

def 한번이동():
    for i in range(8):
        거리 = randint(1,10) * 3
        거북모음[i].forward(거리)

예측한거북 = int(turtle.numinput("거북이 고르기!", "1~8번까지의 거북이 중에 이길 것 같은 거북이의 번호를 입력해주세요! ", minval=1, maxval=8))


#거북 8마리 만들기
for i in range(8):
    print(i)
    거북모음[i] = Turtle()
    거북모음[i].shape("turtle")
    거북모음[i].fillcolor(색깔모음[i])
    거북모음[i].up()
    거북모음[i].speed(4)
    거북모음[i].setpos(-300, 160-(40*i))
    
#결승선 그리기
심판거북 = Turtle()
심판거북.hideturtle()
심판거북.up()
심판거북.setpos(150, 190)
심판거북.down()
심판거북.right(90)
심판거북.forward(350)

    

#목표에 도달 전까지 계속 이동
아직도착못함 = True
while 아직도착못함:
    한번이동()
    for i in range(8):
        # print(거북모음[i].xcor())
        # 아직도착못함 = False
        
        if 거북모음[i].xcor() >= 150:
            아직도착못함 = False
            
            이긴거북 = 0
            
            if 거북모음[i-1].xcor() < 거북모음[i].xcor():
                이긴거북 = i
                
                if (이긴거북 + 1) == 예측한거북:
                    거북모음[i].write(f" 이겼습니다! 당신이 선택한 {이긴거북 + 1 } 번 {색깔모음[i]} 색 거북이 우승했습니다! ")
                    break
                else:
                    거북모음[i].write(f"당신이 졌습니다! {이긴거북 + 1 } 번 {색깔모음[i]} 색 거북이 우승했습니다! ")
                    break
            
                
        
    
    


        

    
    
    




스크린 = Screen()
스크린.screensize(150,100)
스크린.exitonclick()