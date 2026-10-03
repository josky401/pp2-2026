# 파일명: week4/programming/prob9.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: 터틀 그래픽에서 2개의 거북이 객체 생성 및 이동 (파이썬 익스프레스 09번)
# 설계:
#   - turtle 모듈 활용
#   - 2개의 거북이 객체(t1, t2) 생성
#   - t1은 원 모양(circle), t2는 거북이 모양(turtle)으로 설정 및 각자 위치 이동
#   - test_prob9(): 터틀 객체 생성 후 서로 다른 방향/경로로 움직이는 동작 수행

import turtle

def test_prob9():
    t1 = turtle.Turtle()
    t1.shape("turtle")
    
    t2 = turtle.Turtle()
    t2.shape("circle")
     
    t1.forward(100)
    t1.right(90)
    t1.forward(20)
    t1.left(90)
    t1.forward(100)
 
    t2.left(180)
    t2.forward(100)
    t2.right(90)
    t2.forward(20)
    t2.left(90)
    t2.forward(100)
    
    turtle.done()


if __name__ == "__main__":
    test_prob9()