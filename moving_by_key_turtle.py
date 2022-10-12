from turtle import Turtle, Screen

거북 = Turtle()
스크린 = Screen()


def 앞으로():
    거북.forward(10)
    
def 뒤로():
    거북.backward(10)
    
def 시계반대회전():
    거북.left(5)

def 시계회전():
    거북.right(5)
    
def 지우기():
    거북.clear()
    거북.up()
    거북.home()
    거북.down()

스크린.listen()
스크린.onkeypress(key="w", fun=앞으로)
스크린.onkeypress(key="s", fun=뒤로)
스크린.onkeypress(key="a", fun=시계반대회전)
스크린.onkeypress(key="d", fun=시계회전)
스크린.onkey(key="c", fun=지우기)
#스크린.onkey(key="a", fun=시계반대회전)
스크린.exitonclick()