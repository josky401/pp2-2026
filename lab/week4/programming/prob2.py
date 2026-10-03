# 파일명: week4/programming/prob2.py
# 작성자: 조하늘
# 작성일: 2026-10-03
# 문제: Rocket 클래스 구현 (파이썬 익스프레스 02번)
# 설계:
#   - Rocket 클래스: x, y 좌표 속성 (기본값 0 설정)
#   - 메서드: __init__, __str__, moveUp (y좌표 1 증가)
#   - test_prob2(): Rocket 객체 생성 및 moveUp 동작 검증

class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def moveUp(self):
        self.y += 1

    def __str__(self):
        return f"Rocket(x={self.x}, y={self.y})"


def test_prob2():
    myRocket = Rocket()
    print("로켓의 높이:", myRocket.y)

    myRocket.moveUp()
    print("로켓의 높이:", myRocket.y)


if __name__ == "__main__":
    test_prob2()